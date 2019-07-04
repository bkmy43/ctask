import random
import sys
import os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(myPath + '/../src')

from tweefetcher import fetch_tweets
from settings import DEFAULT_TEST_USER


class TestTweefetcher():
    def test_tweet_fetching(self, user=DEFAULT_TEST_USER):
        """
        Test that getting something from Twitter API works
        """
        result = fetch_tweets(user)
        assert result

    def test_tweet_fetching_limit(self, user=DEFAULT_TEST_USER):
        """
        Test that limiting number of tweets works while getting data from Twitter API
        """
        for _ in range(3):
            limit = random.randint(3, 10)
            result = fetch_tweets(user, limit)
            assert len(result) == limit

    def test_tweet_saving(self):
        pass

    def test_twitter_user_saving(self):
        pass


