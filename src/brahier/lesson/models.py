from django.db import models
from django.contrib.auth.models import User
from brahier.horse.models import import Horse

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    day = models.PositiveSmallIntegerField()
    time = models.TimeField()
    duration = models.IntegerField()
    type = models.CharField(max_lenght=255, blank=True)
    max_places = models.IntegerField()

class Event(models.Model):
    type = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(User)
    lesson = models.ForeignKey(Lesson)
    horse = models.ForeignKey(Horse)