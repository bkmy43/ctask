import unittest
import random
import sys
from tweefetcher import fetch_tweets

# sys.path.append(f'{os.path.dirname(os.path.abspath(__file__))}/../src/')
import settings as s

class TestTweefetcher(unittest.TestCase):
    def test_tweet_fetching(self, user=s.DEFAULT_TEST_USER):
        """
        Test that getting something from Twitter API works
        """
        result = fetch_tweets(user)
        self.assertIsNotNone(result)

    def test_tweet_fetching_limit(self, user=s.DEFAULT_TEST_USER):
        """
        Test that limiting number of tweets works while getting data from Twitter API
        """
        for _ in range(3):
            limit = random.randint(3, 10)
            result = fetch_tweets(user, limit)
            self.assertEqual(len(result), limit)


if __name__ == '__main__':
    unittest.main()
