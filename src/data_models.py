from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from tweepy.models import Status

Base = declarative_base()


class TwitterUser(object):
    """
    Basic class to store twitter user data: contains attributes, which are common for
    Tweepy API TwitterUser object and sqlalchemy Data Model Class.
    """
    def __init__(self, id_str, name, screen_name, location, description,
                 followers_count, friends_count, favourites_count, statuses_count, created_at):
        self.id_str = id_str
        self.name = name
        self.screen_name = screen_name
        self.location = location
        self.description = description
        self.followers_count = followers_count
        self.friends_count = friends_count
        self.favourites_count = favourites_count
        self.statuses_count = statuses_count
        self.created_at = created_at


class TwitterUserModel(Base, TwitterUser):
    """
    ORM Model, used to create twitter_user table and to access the data stored there
    """
    __tablename__ = 'twitter_user'

    id_str = Column('id_str', String(20), comment='user id (str)', primary_key=True)
    name = Column('name', String(50), comment='user name', nullable=False)
    screen_name = Column('screen_name', String(15), comment='user screen name', nullable=False)
    location = Column('location', String(), comment='user location')
    description = Column('description', String(), comment='user description of the account')
    followers_count = Column('followers_count', BigInteger(), comment='number of followers')
    friends_count = Column('friends_count', BigInteger(), comment='number of friends')
    favourites_count = Column('favourites_count', BigInteger(), comment='number of tweets this user has liked (lifetime)')
    statuses_count = Column('statuses_count', BigInteger(), comment='number of tweets (incl re-tweets) this user has posted (lifetime)')
    created_at = Column('created_at', DateTime(), comment='user creation timestamp')

    def __repr__(self):
        return '\n'.join(f'{field} = {getattr(self, field)}' for field in dir(TwitterUserModel)
                         if not field.startswith('_') and field != 'metadata')


class Tweet(object):
    """
    Basic class to store tweet data: contains attributes, which are common for
    Tweepy API Tweet object and sqlalchemy Data Model Class.
    """
    def __init__(self, created_at, id_str, text, in_reply_to_status_id_str, in_reply_to_user_id_str,
                 is_quote_status, retweet_count, favorite_count, lang):
        self.created_at = created_at
        self.id_str = id_str
        self.text = text
        self.in_reply_to_status_id_str = in_reply_to_status_id_str
        self.in_reply_to_user_id_str = in_reply_to_user_id_str
        self.is_quote_status = is_quote_status
        self.retweet_count = retweet_count
        self.favorite_count = favorite_count
        self.lang = lang


class TweetAPIWrapper(Tweet):
    """
    Wrapper to access needed fields from API response while initiating TweetModel
    """
    def __init__(self, status: Status):
        
        self.__dict__ = Tweet.__dict__.copy()


class TweetModel(Base, Tweet):
    """
    ORM Model, used to create tweet table and to access the data stored there
    """
    __tablename__ = 'tweet'

    created_at = Column('created_at', DateTime(), comment='tweet creation timestamp')
    id_str = Column('id_str', String(20), comment='tweet id (str)', primary_key=True)
    text = Column('text', String(), comment='tweet text', nullable=False)
    in_reply_to_status_id_str = Column('in_reply_to_status_id_str', String(20), comment='if this is a reply, contains id of the original tweet')
    in_reply_to_user_id_str = Column('in_reply_to_user_id_str', String(20), comment='if this is a reply, contains id of the original author')
    is_quote_status = Column('is_quote_status', Boolean(), comment='flags if this is a quote')
    retweet_count = Column('retweet_count', BigInteger(), comment='how many times this tweet was re-tweeted')
    favorite_count = Column('favorite_count', BigInteger(), comment='how many times this tweed was liked')
    lang = Column('lang', String(5), comment='language')
    # user_id_str = Column('user_id_str', String(20), comment='user id (str)')

    def __init__(self, tweet: Tweet):
        self.__dict__ = tweet.__dict__.copy()
        self.user_id_str = 'abc'

    def __repr__(self):
        return '\n'.join(f'{field} = {getattr(self, field)}' for field in dir(TweetModel)
                         if not field.startswith('_') and field != 'metadata')



