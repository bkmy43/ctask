#!.venv/bin/python
import os
import tweepy
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

import settings
import data_models
import sql_queries

SCRIPT_NAME = os.path.basename(__file__)

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
    arg_parser.add_argument('-v', '--version', action='version', version=f'{SCRIPT_NAME} '
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


def fetch_user(username, api=None):
    """
    Fetches a set of tweets for the given user from Twitter API
    """
    try:
        if not api:
            api = init_twitter_api()
        user = api.get_user(screen_name=username)
        return user
    except Exception as e:
        print(f'Something went wrong while fetching tweets from the API...\n{e}')
        return None


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


def print_tweets(tweets, detailed=False):
    """
    Prints a set of tweet in a short or in a detailed format, depending on print_details parameter value
    """
    for tweet in tweets:
        print_tweet(tweet, detailed)


def save_tweet(tweet, db_session=None):
    """
    Saves tweet to the database, depending on existence of this tweet's id in the database, makes INSERT or UPDATE
    """
    try:
        if not db_session:
            db_session = init_db_session()

        db_session.merge(data_models.Tweet(tweet))
        db_session.commit()
    except Exception as e:
        raise e


def save_tweets(tweets, db_session=None):
    """
    Gets set of tweets as a parameter, executes save_tweet() for each of them
    """
    try:
        saved_users = []
        for tweet in tweets:
            if tweet.user.screen_name not in saved_users:
                user = fetch_user(tweet.user.screen_name)
                save_user(user, db_session)
                saved_users.append(tweet.user.screen_name)
            save_tweet(tweet, db_session)
        return True
    except Exception as e:
        print(f'Something went wrong while saving tweets to the database...\n{e}')
        return False


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
        print(f'Something went wrong while saving users to the database...\n{e}')
        return False


def show_statistics(db_session=None):
    """
    Shows basic user statistics for all users in the database
    """
    try:
        if not db_session:
            db_session = init_db_session()

        stats = db_session.execute(text(sql_queries.SQL['user_statistics']))
        column_names = stats.keys()
        for row in stats:
            for col_num, col_value in enumerate(row):
                col_name = column_names[col_num]
                sep = ':\t' if len(col_name) > 14 else ':\t\t'
                print(f'{col_name}{sep}{col_value}')
            print('-' * 43)
        return True
    except Exception as e:
        raise e


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
        print(f'Fetching the last {args.limit} tweets for the user {args.username} from Twitter API...')
        tweets = fetch_tweets(args.username, args.limit)
        print(f'{len(tweets)} tweets for the user {args.username} successfully fetched.\n'
              f'Saving them to the database...')
        save_tweets(tweets)
        print(f'Done')
    elif args.action == 'show':
        print('Not implemented yet')
    elif args.action == 'stats':
        show_statistics()
    else:
        print(f'ERROR: No valid action specified, please run "{SCRIPT_NAME} -h" for help')


if __name__ == "__main__":
    main()
