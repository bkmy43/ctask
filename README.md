# Description
Fetches tweets for a specified user from the Twitter API, stores them in local
database and provides the possibility to display them later along with some
basic statistics

# Installation
pip install -r requirements.txt

# Usage
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
