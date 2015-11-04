from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from datetime import datetime

class IdeaPost(models.Model):
    title = models.CharField(max_length = 60)
    company = models.CharField(max_length = 60)
    description = models.TextField(max_length = 100000)
    author = models.CharField(max_length = 60)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):

    content = models.TextField(max_length = 100000)
    idea_post = models.ForeignKey(IdeaPost)
    author = models.CharField(max_length = 60)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.author + " : " + self.content[:10] + " ..."

