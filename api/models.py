# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Sloat(models.Model):
    username = models.CharField(max_length=255)
    start_time = models.DateTimeField()

class Sloats(models.Model):
    username = models.CharField(max_length=255)
    start_time = models.DateTimeField(unique=True)
    booked_by_user = models.CharField(max_length=255)

class MeetingNotes(models.Model):
    start_by_user = models.CharField(max_length=255)
    sloats = models.ForeignKey(Sloats)
    status = models.CharField(max_length=20)
    
class Tasks(models.Model):
    task = models.CharField(max_length=255)
    meeting = models.ForeignKey(MeetingNotes)
    task_from_user = models.CharField(max_length=255)
    task_to_user = models.CharField(max_length=255)
