from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TwitterUser(Base):
    __tablename__ = 'twitter_user'

    id_str = Column('id_str', String(20), comment='user id (str)', primary_key=True)
    name = Column('name', String(50), comment='user name', nullable=False)
    screen_name = Column('screen_name', String(15), comment='user screen name', nullable=False)
    location = Column('location', String(), comment='user location')
    description = Column('description', String(), comment='user description of the account')
    followers_count = Column('followers_count', BigInteger(), comment='number of followers')
    friends_count = Column('friends_count', BigInteger(), comment='number of friends')
    favourites_count = Column('favourites_count', BigInteger(),
                              comment='number of tweets this user has liked (lifetime)')
    statuses_count = Column('statuses_count', BigInteger(),
                            comment='number of tweets (incl re-tweets) this user has posted (lifetime)')
    created_at = Column('created_at', DateTime(), comment='user creation timestamp')

    def __init__(self, tweepy_user):
        self.id_str = tweepy_user.id_str
        self.name = tweepy_user.name
        self.screen_name = tweepy_user.screen_name
        self.location = tweepy_user.location
        self.description = tweepy_user.description
        self.followers_count = tweepy_user.followers_count
        self.favourites_count = tweepy_user.favourites_count
        self.statuses_count = tweepy_user.statuses_count
        self.created_at = tweepy_user.created_at

    def __repr__(self):
        return '\n'.join(f'{field} = {getattr(self, field)}' for field in dir(TwitterUser)
                         if not field.startswith('_') and field != 'metadata')


class Tweet(Base):
    __tablename__ = 'tweet'

    created_at = Column('created_at', DateTime(), comment='tweet creation timestamp')
    id_str = Column('id_str', String(20), comment='tweet id (str)', primary_key=True)
    text = Column('text', String(), comment='tweet text', nullable=False)
    in_reply_to_status_id_str = Column('in_reply_to_status_id_str', String(20),
                                       comment='if this is a reply, contains id of the original tweet')
    in_reply_to_user_id_str = Column('in_reply_to_user_id_str', String(20),
                                     comment='if this is a reply, contains id of the original author')
    is_quote_status = Column('is_quote_status', Boolean(), comment='flags if this is a quote')
    retweet_count = Column('retweet_count', BigInteger(), comment='how many times this tweet was re-tweeted')
    favorite_count = Column('favorite_count', BigInteger(), comment='how many times this tweed was liked')
    lang = Column('lang', String(5), comment='language')
    user_id_str = Column('user_id_str', String(20), comment='user id (str)')

    def __init__(self, tweepy_tweet):
        self.created_at = tweepy_tweet.created_at
        self.id_str = tweepy_tweet.id_str
        self.text = tweepy_tweet.text
        self.in_reply_to_status_id_str = tweepy_tweet.in_reply_to_status_id_str
        self.in_reply_to_user_id_str = tweepy_tweet.in_reply_to_user_id_str
        self.is_quote_status = tweepy_tweet.is_quote_status
        self.retweet_count = tweepy_tweet.retweet_count
        self.favorite_count = tweepy_tweet.favorite_count
        self.lang = tweepy_tweet.lang
        self.user_id_str = tweepy_tweet.user.id_str

    def __repr__(self):
        return '\n'.join(f'{field} = {getattr(self, field)}' for field in dir(Tweet)
                         if not field.startswith('_') and field != 'metadata')
