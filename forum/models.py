from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

# Modelling a web forum consisting of discussion boards, topics,posts and users


class Board(models.Model):

    name = models.CharField(max_length=30, unique=True)  # name of specific forum should be unique
    description = models.TextField(max_length=4000)

    def __str__(self):

        return self.name

    def get_absolute_url(self):
        
        return reverse('board_details', kwargs={'name': self.name})


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')  # Board that this topics belongs to
    starter = models.ForeignKey(User, related_name='topics')  # user who owns this topic

    def __str__(self):

        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')  # Topic that this post relates to
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User,null=True,related_name='+')