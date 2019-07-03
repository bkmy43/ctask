from sqlalchemy import *
import settings

metadata = MetaData()

tweeter_user = Table('tweeter_user', metadata,
    Column('id_str', String(20), comment='user id (str)', primary_key=True),
    Column('name', String(50), comment='user name', nullable=False),
    Column('screen_name', String(15), comment='user screen name', nullable=False),
    Column('location', String(), comment='user location'),
    Column('description', String(), comment='user description of the account'),
    Column('followers_count', BigInteger(), comment='number of followers'),
    Column('friends_count', BigInteger(), comment='number of friends'),
    Column('favourites_count', BigInteger(), comment='number of tweets this user has liked (lifetime)'),
    Column('statuses_count', BigInteger(), comment='number of tweets (incl re-tweets) this user has posted (lifetime)'),
    Column('created_at', DateTime(), comment='user creation timestamp')
)



