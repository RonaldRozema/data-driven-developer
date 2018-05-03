from django.db import models


class CvEntry(models.Model):

    text = models.CharField(max_length=10000)