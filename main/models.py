from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')
    date = models.DateField()

class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='team/')

class Trivia(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    date = models.DateField()
