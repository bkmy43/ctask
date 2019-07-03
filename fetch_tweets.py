import tweepy
import argparse

consumer_key = 't8bhToaY4LevkBjvS355A9pfu'
consumer_secret = '2315cTZYr7OQmoDytBWpuothCAakOYER7pE6fF3ZLUXeAC8rkz'
access_token_key = '882165583911038976-XgiJxECv0cCsg2Ech6HmzPuzsD1zILp'
access_token_secret = 'e9puaP5NBK0JWjEUXCE214yc2CXpkgC1zPMzmgDs5ZLc5'

TWEET_PER_PERSON_LIMIT_DEFAULT = 5
VERSION = '1.0'
BUILD_DATE = '03.07.2019'


def get_tweets(username, limit=TWEET_PER_PERSON_LIMIT_DEFAULT):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name=username)

    test_tweet = tweets[0]
    for key in test_tweet._json.keys():
        print("{} : {}".format(key, test_tweet._json[key]))

    tweets = [tweet.text for tweet in tweets]
    print(list(tweets))


def main():
    arg_parser = argparse.ArgumentParser(description='Fetches tweets for a specified user from the Twitter API, '
                                                     'stores them in local database and provides the possibility '
                                                     'to display them later along with some basic statistics')
    arg_parser.add_argument('-v', '--version', action='version', version='%(prog)s v.{} {}'
                            .format(VERSION, BUILD_DATE))
    arg_parser.add_argument('-a', '--action', action='store', help='Action to do: fetch/get/stats')
    arg_parser.add_argument('-u', '--username', action='store', help='Username to get the tweets for')
    arg_parser.add_argument('-l', '--limit', action='store', help='Limit for the number of tweets ({} by default'
                            .format(TWEET_PER_PERSON_LIMIT_DEFAULT))

    args = arg_parser.parse_args()
    print(args)

    # get_tweets('navalny')


if __name__ == "__main__":
    main()
