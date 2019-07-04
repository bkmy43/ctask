import random
import sys
import os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(myPath + '/../src')

from tweet_fetcher import fetch_tweets, save_tweet
from settings import DEFAULT_TEST_USER, DEFAULT_NUMBER_OF_TWEETS_FOR_TESTS


class TestTweetfetcher():
    def test_tweet_fetching(self, user=DEFAULT_TEST_USER):
        """
        Test that getting something from Twitter API works
        """
        assert fetch_tweets(user)  # if the function returns non empty object, we assume the connection to API works

    def test_tweet_fetching_limit(self, user=DEFAULT_TEST_USER, rep=DEFAULT_NUMBER_OF_TWEETS_FOR_TESTS):
        """
        Test that limiting number of tweets works while getting data from Twitter API
        """
        for _ in range(rep):
            limit = random.randint(3, 10)
            result = fetch_tweets(user, limit)
            assert len(result) == limit

    def test_tweet_saving(self, user=DEFAULT_TEST_USER, rep=DEFAULT_NUMBER_OF_TWEETS_FOR_TESTS):
        """
        Test that saving of tweets to the database works
        """
        assert save_tweet(fetch_tweets(user, 1)[0])

    def test_twitter_user_saving(self):
        pass


