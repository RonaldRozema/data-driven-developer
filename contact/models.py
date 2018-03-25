from django.db import models

import datetime


class ContactFormModel(models.Model):

    subject = models.CharField(max_length=40)
    contact_date = models.DateTimeField(default=datetime.datetime.now())
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.subject