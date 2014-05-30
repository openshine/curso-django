from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    created_by = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    text = models.TextField()


class Comment(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    text = models.TextField()
