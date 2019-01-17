# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from . import forms
from .models import Task,Subtask
from django.http import HttpResponse 

def task_views(request):
    if request.method == 'POST':
        form = forms.CreateTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task:taskview')
    else:
        subforms = forms.CreateSubTask()
        tasks = Task.objects.all()      
        form = forms.CreateTask()
        subtasks = Subtask.objects.all()
        return render(request,'task/task_view.html',{'form':form,'tasks':tasks,'subforms':subforms,'subtasks':subtasks})


def sub_add(request,title):
        print("CALLEDhiuhi")
        if request.method== 'POST':
                sub = Subtask()
                title=title.encode("ascii","replace")
                task = Task.objects.get(title=title)
                sub.title=task
                subform = forms.CreateSubTask(request.POST)
                
                if subform.is_valid():
                        sub.subtask=subform.cleaned_data.get("subtask")

                        sub.save()
                        return redirect('task:taskview')
                else:
                        return HttpResponse("ERROR")
        else:
                        return HttpResponse(title) 


def sub_del(request,subtask,task):
        if request.method=='POST':
                task = Task.objects.get(title=task)
                subtask = Subtask.objects.get(title=task,subtask=subtask)
                subtask.delete()
                return redirect('task:taskview')



def task_del(request,tasktitle):
        print("CALLED")
        if request.method=='POST':
                task = Task.objects.get(title=tasktitle)
                task.delete()
                return redirect('task:taskview')

def task_edit(request,taskedit):
        if request.method=='POST':
                form = Task.objects.get(title=taskedit)
                form = forms.CreateTask(initial={'title':taskedit})
                return render(request,'task/update.html',{'form':form,'tasktitle':taskedit})

def task_final(request,taskfinal):
        if request.method=='POST':
                form =forms.CreateTask(request.POST)
                if form.is_valid():
                        tasktitle=form.cleaned_data.get("title")
                        Task.objects.filter(title=taskfinal).update(title=tasktitle)
                        return redirect('task:taskview')

                
                


# Create your views here.
