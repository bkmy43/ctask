import unittest
from tweefetcher import fetch_tweets

class TestTweetFetching(unittest.TestCase):
    def test_list_int(self):
        """
        Test that getting a list of tweets from Twitter API works
        """
        username = 'navalny' # Alexei Anatolievich Navalny is a Russian lawyer and political activist
        # result = tf.fetch_tweets(username)
        print(tweefetcher.consumer_key)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()