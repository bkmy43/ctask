from django.db import models


class User(models.Model):
    pass

class Tweet(models.Model):
    created_at = models.DateTimeField('tweet creation timestamp')
    id = models.BigIntegerField('tweet id') # according to tweeter api docs signed 64bit int should be enough
    id_str = models.CharField('tweet id (str)', max_length=20) # 20 digits should be sufficient (see previous comment)
    text = models.CharField('tweet text')
    truncated = models.BooleanField('flags if the original text was truncated')
    in_reply_to_status_id_str = models.CharField('if this is a reply, contains the id of the original tweet', max_length=20)
    in_reply_to_user_id_str = models.CharField('if this is a reply, contains the id (str) of the author of original tweet', max_length=20)
    user_id_str = models.CharField('user id (str)', max_length=20)
    coordinates = models.CharField('geo json with coordinates')
    quoted_status_id_str = models.CharField('if this is a quote, contains the id of the original tweet', max_length=20)
    quote_count = models.CharField('if this is a quote, contains the id of the original tweet', max_length=20)
