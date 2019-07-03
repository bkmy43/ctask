from orator import DatabaseManager, Model, Schema
import settings as s


db = DatabaseManager(s.db_config)
schema = Schema(db)


def create_tables():
    with schema.create('user') as table:
        table.char('id_str', 20)                # user id (str)
        table.char('name', 50)                  # user name
        table.char('screen_name', 15)           # user screen name
        table.char('location')                  # user location
        table.char('description')               # user description of the account
        table.big_integer('followers_count')    # number of followers
        table.big_integer('friends_count')      # number of friends
        table.big_integer('favourites_count')   # number of tweets this user has liked (lifetime)
        table.big_integer('statuses_count')     # number of tweets (incl re-tweets) this user has posted (lifetime)
        table.datetime('created_at')            # user creation timestamp


# Model.set_connection_resolver(db)
# create_tables()


