# Generated by Django 2.0.2 on 2018-03-25 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=40)),
                ('contact_date', models.DateTimeField(verbose_name='date contacted')),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
    ]
