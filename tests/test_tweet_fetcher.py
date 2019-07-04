import random
import sys
import os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(myPath + '/../src')

from tweet_fetcher import fetch_tweets, save_tweet
from settings import NUMBER_OF_TWEETS_FOR_TESTS, TEST_USERS


class TestTweetfetcher():
    def test_tweet_fetching(self):
        """
        Test that getting something from Twitter API works
        """
        assert fetch_tweets(user=random.choice(TEST_USERS))  # if the function returns non empty object,
                                                             # we assume the connection to API works

    def test_tweet_fetching_limit(self):
        """
        Test that limiting number of tweets works while getting data from Twitter API
        """
        for _ in range(NUMBER_OF_TWEETS_FOR_TESTS):
            limit = random.randint(5, 10)
            result = fetch_tweets(user=random.choice(TEST_USERS), limit=limit)
            assert len(result) == limit

    def test_tweet_saving(self):
        """
        Test that saving of tweets to the database works
        """
        assert save_tweets(fetch_tweets(user=random.choice(TEST_USERS), limit=1)[0])

    def test_twitter_user_saving(self):
        pass


