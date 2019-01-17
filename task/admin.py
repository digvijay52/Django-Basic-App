# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Task,Subtask

admin.site.register(Task)
admin.site.register(Subtask)
# Register your models here.
