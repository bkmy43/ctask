#!../.venv/bin/python

import tweepy
import argparse
import os
print()

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN_KEY = os.environ['ACCESS_TOKEN_KEY']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

SCRIPT_NAME = os.path.basename(__file__)
TWEETS_LIMIT = 5
VERSION = '1.0'
BUILD_DATE = '03.07.2019'


def init_tweeter_api(key=CONSUMER_KEY, secret=CONSUMER_SECRET,
                     token_key=ACCESS_TOKEN_KEY, token_secret=ACCESS_TOKEN_SECRET):
    """
    Creates a connection to the Twitter API and returns it as an object
    """
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)


def fetch_tweets(username, limit=TWEETS_LIMIT):
    """
    Fetches a set of tweets for the given user from Twitter API
    """
    api = init_tweeter_api()
    tweets = api.user_timeline(screen_name=username, count=limit)
    return tweets


def print_tweet(tweet, print_details=False):
    """
    Prints a given tweet in a short or in a detailed format, depending on print_details parameter value
    """
    if print_details:
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


def get_arguments():
    """
    Parses command line arguments of tweefetcher and returns the results as an object
    """
    arg_parser = argparse.ArgumentParser(description='Fetches tweets for a specified user from the Twitter API, '
                                                     'stores them in local database and provides the possibility '
                                                     'to display them later along with some basic statistics')
    arg_parser.add_argument('-v', '--version', action='version', version=f'{SCRIPT_NAME} v.{VERSION} {BUILD_DATE}')
    arg_parser.add_argument('-a', '--action', action='store', help='Action to do: fetch/get/stats')
    arg_parser.add_argument('-u', '--username', action='store', help='Username to get the tweets for')
    arg_parser.add_argument('-l', '--limit', action='store',
                            help=f'Limit for the number of tweets ({TWEETS_LIMIT} by default')

    return arg_parser.parse_args()


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
        print_tweets(fetch_tweets(args.username, args.limit), print_details=True)
    elif args.action == 'get':
        pass
    elif args.action == 'stats':
        pass
    else:
        print(f'ERROR: No valid action specified, please run "{SCRIPT_NAME} -h" for help')


if __name__ == "__main__":
    main()
