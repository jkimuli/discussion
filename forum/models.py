from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.text import Truncator

# Create your models here.

# Modelling a web forum consisting of discussion boards, topics,posts and users


class Board(models.Model):

    name = models.CharField(max_length=30, unique=True)  # name of specific forum should be unique
    description = models.TextField(max_length=4000)

    def __str__(self):

        return self.name

    def get_absolute_url(self):
        
        return reverse('board_details', kwargs={'name': self.name})

    def get_topic_count(self):

        return self.topics.count()

    def get_posts_count(self):

        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')  # Board that this topics belongs to
    starter = models.ForeignKey(User, related_name='topics')  # user who owns this topic
    views = models.PositiveIntegerField(default=0)

    def __str__(self):

        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')  # Topic that this post relates to
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')  # you can return numbers of posts created by this user
    updated_by = models.ForeignKey(User,null=True,related_name='+')

    def __str__(self):

        truncated_message = Truncator(self.message)

        return truncated_message.chars(30) # truncate to the first 30 chars