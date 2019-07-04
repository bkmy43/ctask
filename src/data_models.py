from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TweeterUser(Base):
    __tablename__ = 'tweeter_user'

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

    # def __repr__(self):
    #     return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)


# metadata = MetaData()
#
# tweeter_user = Table('tweeter_user', metadata,
#     Column('id_str', String(20), comment='user id (str)', primary_key=True),
#     Column('name', String(50), comment='user name', nullable=False),
#     Column('screen_name', String(15), comment='user screen name', nullable=False),
#     Column('location', String(), comment='user location'),
#     Column('description', String(), comment='user description of the account'),
#     Column('followers_count', BigInteger(), comment='number of followers'),
#     Column('friends_count', BigInteger(), comment='number of friends'),
#     Column('favourites_count', BigInteger(), comment='number of tweets this user has liked (lifetime)'),
#     Column('statuses_count', BigInteger(), comment='number of tweets (incl re-tweets) this user has posted (lifetime)'),
#     Column('created_at', DateTime(), comment='user creation timestamp')
# )
#
# tweet = Table('tweet', metadata,
#     Column('created_at', DateTime(), comment='tweet creation timestamp'),
#     Column('id_str', String(20), comment='tweet id (str)', primary_key=True),
#     Column('text', String(), comment='tweet text', nullable=False),
#     Column('in_reply_to_status_id_str', String(20), comment='if this is a reply, contains id of the original tweet'),
#     Column('in_reply_to_user_id_str', String(20), comment='if this is a reply, contains id of the original author'),
#     Column('user_id_str', String(20), comment='user id (str)'),
#     Column('coordinates', String(), comment='geo json with coordinates'),
#     Column('quoted_status_id_str', String(20), comment='if this is a quote, contains the id of the original tweet'),
#     Column('retweet_count', BigInteger(), comment='how many times this tweet was re-tweeted'),
#     Column('favorite_count', BigInteger(), comment='how many times this tweed was liked'),
#     Column('lang', String(5), comment='language')
# )



