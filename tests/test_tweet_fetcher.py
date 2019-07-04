import random
import sys
import os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.append(myPath + '/../src')

from tweet_fetcher import fetch_tweets, save_tweets, save_user, fetch_user, print_tweets
from settings import NUMBER_OF_TEST_REPETITIONS, TEST_USERS


class TestTweetfetcher():
    def test_tweet_fetching(self):
        """
        Test that getting something from Twitter API works
        """
        assert fetch_tweets(username=random.choice(TEST_USERS))  # if the function returns non empty object,
                                                                 # we assume the connection to API works
    def test_tweet_fetching_and_printing(self):
        """
        Test that getting something from Twitter API works
        """
        tweets = fetch_tweets(username=random.choice(TEST_USERS))
        assert tweets
        print_tweets(tweets=tweets, detailed=True)


    def test_user_fetching(self):
        """
        Test that getting something from Twitter API works
        """
        assert fetch_user(username=random.choice(TEST_USERS))

    def test_tweet_fetching_limit(self):
        """
        Test that limiting number of tweets works while getting data from Twitter API
        """
        for _ in range(NUMBER_OF_TEST_REPETITIONS):
            limit = random.randint(5, 10)
            result = fetch_tweets(username=random.choice(TEST_USERS), limit=limit)
            assert len(result) == limit

    def test_tweet_saving(self):
        """
        Test that saving of tweets to the database works
        """
        for _ in range(NUMBER_OF_TEST_REPETITIONS):
            limit = random.randint(5, 10)
            assert save_tweets(fetch_tweets(username=random.choice(TEST_USERS), limit=limit))

    def test_twitter_user_saving(self):
        """
         Test that saving of twitter users to the database works
         """
        for _ in range(NUMBER_OF_TEST_REPETITIONS):
            assert save_user(fetch_user(username=random.choice(TEST_USERS)))

