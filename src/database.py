from sqlalchemy import *
import datetime

import settings
import data_models
from sqlalchemy.orm import sessionmaker

engine = create_engine(f'postgresql://{settings.PG_USER}:{settings.PG_PASSWORD}@{settings.PG_HOST}:'
                       f'{settings.PG_PORT}/{settings.PG_DATABASE}')

Session = sessionmaker(bind=engine)
session = Session()

data_models.Base.metadata.create_all(engine)

test_user = data_models.TweeterUser(
    id_str = 'aaaa',
    name = 'user name',
    screen_name = 'screen_name',
    location = 'location',
    description = 'description',
    followers_count = 0,
    friends_count = 0,
    favourites_count = 0,
    statuses_count = 0,
    created_at = None #datetime.datetime()
)

session.add(test_user)
session.commit()