# Description
Fetches tweets for a specified user from the Twitter API, stores them in local
database and provides the possibility to display them later along with some
basic statistics

# Installation
```
pip install -r requirements.txt
```

# Environment
```shellscript
export CONSUMER_KEY='... your consumer key ...'
export CONSUMER_SECRET='... your consumer secret ...'
export ACCESS_TOKEN_KEY='... your access token key ...'
export ACCESS_TOKEN_SECRET='... your access token secret ...'

export PG_HOST='...'
export PG_PORT='...'
export PG_USER='...'
export PG_PASSWORD='...'
```
# Usage
```
tweefetcher.py [-h] [-v] [-a ACTION] [-u USERNAME] [-l LIMIT]

optional arguments:

  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -a ACTION, --action ACTION
                          Action to do: fetch/get/stats
  -u USERNAME, --username USERNAME
                          Username to get the tweets for
  -l LIMIT, --limit LIMIT
                          Limit for the number of tweets (5 by default)
```
