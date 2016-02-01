from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=50000)
    pub_date = models.DateTimeField('date published')
