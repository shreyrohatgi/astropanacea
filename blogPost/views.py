# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response

def loadHomePage(request):
    return render_to_response(os.path.join(os.getcwd(),'templates','home_django.html'))


"""
/Users/vaibhavarora/Desktop/PycharmProjects/paxcelProjects/web/astropanacea/templates/home_django.html

"""