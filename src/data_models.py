from orator import Model

class User(Model):
    pass

class Tweet(Model):
    pass


# from django.db import models
#
#
# class User(models.Model):
#     id_str = models.CharField('user id (str)', max_length=20)  # according to api docs, 20 digits should be sufficient
#     name = models.CharField('user name', max_length=50)
#     screen_name = models.CharField('user screen name', max_length=15)
#     location = models.CharField('user location')
#     description = models.CharField('user description of the account')
#     followers_count = models.BigIntegerField('number of followers')
#     friends_count = models.BigIntegerField('number of friends')
#     favourites_count = models.BigIntegerField('number of tweets this user has liked (lifetime)')
#     statuses_count = models.BigIntegerField('number of tweets (incl re-tweets) this user has posted (lifetime)')
#     created_at = models.DateField('user creation timestamp')
#
#
# class Tweet(models.Model):
#     created_at = models.DateTimeField('tweet creation timestamp')
#     id_str = models.CharField('tweet id (str)', max_length=20)  # according to api docs, 20 digits should be sufficient
#     text = models.CharField('tweet text')
#     truncated = models.BooleanField('flags if the original text was truncated')
#     in_reply_to_status_id_str = models.CharField('if this is a reply, contains id of the original tweet', max_length=20)
#     in_reply_to_user_id_str = models.CharField('if this is a reply, contains id of the original author', max_length=20)
#     user_id_str = models.CharField('user id (str)', max_length=20)
#     coordinates = models.CharField('geo json with coordinates')
#     quoted_status_id_str = models.CharField('if this is a quote, contains the id of the original tweet', max_length=20)
#     retweet_count = models.BigIntegerField('how many times this tweet was re-tweeted')
#     favorite_count = models.BigIntegerField('how many times this tweed was liked')
#     lang = models.CharField('language', max_length=5)

