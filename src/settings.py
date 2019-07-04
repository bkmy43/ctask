import os

# twitter api credentials
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN_KEY = os.environ['ACCESS_TOKEN_KEY']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# database credentials
PG_HOST = 'localhost'
PG_PORT = '5432'
PG_DATABASE = 'tweet_fetcher_db'
PG_USER = 'tweet_fetcher'
PG_PASSWORD = 'tweet_fetcher'

# version
SCRIPT_NAME = os.path.basename(__file__)
VERSION = '1.0'
BUILD_DATE = '03.07.2019'

# default parameters
DEFAULT_TWEETS_LIMIT = 5
TEST_USERS = ('BarackObama', 'navalny', 'ladygaga')
NUMBER_OF_TWEETS_FOR_TESTS = 3

