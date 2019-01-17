from django import forms
from . import models

class CreateTask(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title']


class CreateSubTask(forms.ModelForm):
    class Meta:
        model = models.Subtask
        fields = ['subtask']

class SubTask(forms.ModelForm):
    class Meta:
        model = models.Subtask
        fields = ['title','subtask']