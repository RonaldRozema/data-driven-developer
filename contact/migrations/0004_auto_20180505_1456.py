# Generated by Django 2.0.2 on 2018-05-05 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20180505_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmodel',
            name='contact_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 5, 14, 56, 33, 376437)),
        ),
    ]
