# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def article_list(request):
    return render(request,'articles/article_list.html')


# Create your views here.