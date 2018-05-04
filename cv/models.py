from django.db import models


class Skill(models.Model):
    
    total_percentage = models.IntegerField(default=100)
    mastered_percentage = models.IntegerField(default=0)


class Project(models.Model):
    
    title = models.CharField(max_length=200)
    function = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)


class Resource(models.Model):
    
    link = models.CharField(max_length=250)
    name = models.CharField(max_length=150)


class CvEntry(models.Model):

    text = models.CharField(max_length=10000)
    skills = models.ManyToManyField(Skill)
    projects = models.ManyToManyField(Project)
    resources = models.ManyToManyField(Resource)
