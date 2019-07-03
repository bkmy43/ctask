from django.db import models


class Tweet(models.Model):
    created_at = models.DateTimeField('tweet creation timestamp')
    id = models.BigIntegerField('tweet id')
    id_str = ''
    name = models.CharField('Event Name', max_length=120)

    venue = models.CharField(max_length=120)
    manager = models.CharField(max_length = 60)
    description = models.TextField(blank=True)