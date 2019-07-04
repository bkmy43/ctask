#!.venv/bin/python

import tweepy
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings
import data_models


def init_db_session():
    """
    Creates a database session and returns it as an object
    """
    engine = create_engine(f'postgresql://{settings.PG_USER}:'
                           f'{settings.PG_PASSWORD}@{settings.PG_HOST}:'
                           f'{settings.PG_PORT}/{settings.PG_DATABASE}')
    data_models.Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    return session()


def init_twitter_api(key=settings.CONSUMER_KEY, secret=settings.CONSUMER_SECRET,
                     token_key=settings.ACCESS_TOKEN_KEY, token_secret=settings.ACCESS_TOKEN_SECRET):
    """
    Creates a connection to the Twitter API and returns it as an object
    """
    auth = tweepy.OAuthHandler(key, secret)
    auth.set_access_token(token_key, token_secret)
    return tweepy.API(auth)


def get_arguments():
    """
    Parses command line arguments of tweet_fetcher and returns the results as an object
    """
    arg_parser = argparse.ArgumentParser(description='Fetches tweets for a specified user from the Twitter API, '
                                                     'stores them in local database and provides the possibility '
                                                     'to display them later along with some basic statistics')
    arg_parser.add_argument('-v', '--version', action='version', version=f'{settings.SCRIPT_NAME} '
                                                                         f'v.{settings.VERSION} {settings.BUILD_DATE}')
    arg_parser.add_argument('-a', '--action', action='store', help='Action to do: fetch/get/stats')
    arg_parser.add_argument('-u', '--username', action='store', help='Username to get the tweets for')
    arg_parser.add_argument('-l', '--limit', action='store',
                            help=f'Limit for the number of tweets ({settings.DEFAULT_TWEETS_LIMIT} by default')

    return arg_parser.parse_args()


def fetch_tweets(username, limit=settings.DEFAULT_TWEETS_LIMIT, api=None):
    """
    Fetches a set of tweets for the given user from Twitter API
    """
    if not api:
        api = init_twitter_api()
    tweets = api.user_timeline(screen_name=username, count=limit)
    return tweets


def print_tweet(tweet, detailed=False):
    """
    Prints a given tweet in a short or in a detailed format, depending on print_details parameter value
    """
    if detailed:
        for key in tweet._json.keys():
            print(f'{key} : {tweet._json[key]}')
        print('\n')
    else:
        print(f'{tweet.created_at}: {tweet.text}')


def print_tweets(tweets, print_details=False):
    """
    Prints a set of tweet in a short or in a detailed format, depending on print_details parameter value
    """
    for tweet in tweets:
        print_tweet(tweet, print_details)


def save_tweet(tweet, db_session=None):
    """
    Saves tweet to the database, depending on existence of this tweet's id in the database, makes INSERT or UPDATE
    """
    try:
        if not db_session:
            db_session = init_db_session()

        db_session.merge(data_models.Tweet(tweet))
        db_session.commit()
        return True
    except:
        return False


def save_tweets(tweets, db_session=None):
    """
    Gets set of tweets as a parameter, executes save_tweet() for each of them
    """
    for tweet in tweets:
        save_tweet(tweet, db_session)


def save_user(user, db_session=None):
    """
    Saves user to the database, depending on existence of this user's id in the database, makes INSERT or UPDATE
    """
    try:
        if not db_session:
            db_session = init_db_session()

        db_session.merge(data_models.TwitterUser(user))
        db_session.commit()
        return True
    except Exception as e:
        print(f'Something went wrong while saving to the database...\n{e}')
        return False

def save_users(users, db_session=None):
    """
    Gets set of users as a parameter, executes save_user() for each of them
    """
    for user in users:
        save_user(user, db_session)


def main():
    """
    Depending on the action required by the user (via command line parameters) does one of the following:
     - action = 'fetch'
         Fetches the last tweets of the specified user (the number of tweets can be set by the parameter, default is 5)
         Stores the results in the local database (tweets and user data)
     - action = 'get'
         Gets the tweets of the specified user from the local database
         and displays them in a short or in a detailed format
     - action = 'stats'
         Displays a few statistical values for a specified users
         e.g. total number of tweets in the database, shares of re-tweets and citations, etc
    """
    args = get_arguments()

    if args.action == 'fetch':
        print(f'Fetching the last {args.limit} tweets for the user {args.username} from Twitter API')
        tweets = fetch_tweets(args.username, args.limit)
        for tweet in tweets:
            save_tweet(tweet)
    elif args.action == 'get':
        pass
    elif args.action == 'stats':
        pass
    else:
        print(f'ERROR: No valid action specified, please run "{settings.SCRIPT_NAME} -h" for help')


if __name__ == "__main__":
    main()
