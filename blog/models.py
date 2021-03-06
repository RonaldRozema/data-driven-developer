from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField

class Tag(models.Model):
    
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=100)
    content = RichTextUploadingField(max_length=12000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField()
    is_draft = models.BooleanField(default=True)
    is_public = models.BooleanField(default=False)
    amount_upvotes = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    is_removed = models.BooleanField(default=False)
    times_viewed = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_removed = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content