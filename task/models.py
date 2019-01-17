# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
         return self.title

class Subtask(models.Model):
    title = models.ForeignKey(Task, default=None,on_delete=models.CASCADE)
    subtask = models.CharField(max_length=100) 

    def __str__(self):
         return self.title
    
# Create your models here.
