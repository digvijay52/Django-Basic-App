# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html',{'articles':articles})

def article_details(request,slug):
    return HttpResponse(slug)   
    


# Create your views here.
