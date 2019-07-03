import unittest
import random
from tweefetcher import fetch_tweets

TEST_USER = 'navalny' # Navalny is a Russian political activist who is very active in tweeter

class TestTweefetcher(unittest.TestCase):
    def test_tweet_fetching(self):
        """
        Test that getting something from Twitter API works
        """
        result = fetch_tweets(TEST_USER)
        self.assertIsNotNone(result)


    def test_tweet_fetching_limit(self):
        """
        Test that limiting number of tweets works while getting data from Twitter API
        """
        for _ in range(3):
            limit = random.randint(3, 10)
            result = fetch_tweets(TEST_USER, limit)
            self.assertEqual(len(result), limit)


if __name__ == '__main__':
    unittest.main()
