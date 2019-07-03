import os

# twitter api credentials
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN_KEY = os.environ['ACCESS_TOKEN_KEY']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']

# version
SCRIPT_NAME = os.path.basename(__file__)
VERSION = '1.0'
BUILD_DATE = '03.07.2019'

# default parameters
DEFAULT_TWEETS_LIMIT = 5
DEFAULT_USER = 'navalny'  # Navalny is a Russian political activist who is very active in tweeter
