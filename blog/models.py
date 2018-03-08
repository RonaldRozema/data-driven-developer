from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.CharField(max_length=12000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField()