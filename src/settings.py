import os

# twitter api credentials
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN_KEY = os.environ['ACCESS_TOKEN_KEY']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# database credentials
PG_HOST = os.environ['PG_HOST']
PG_PORT = os.environ['PG_PORT']
PG_DATABASE = os.environ['PG_DATABASE']
PG_USER = os.environ['PG_USER']
PG_PASSWORD = os.environ['PG_PASSWORD']

# version
SCRIPT_NAME = os.path.basename(__file__)
VERSION = '1.0'
BUILD_DATE = '03.07.2019'

# default parameters
DEFAULT_TWEETS_LIMIT = 5
DEFAULT_TEST_USER = 'navalny'  # Navalny is a Russian political activist who is very active in tweeter
DEFAULT_NUMBER_OF_TWEETS_FOR_TESTS = 3

