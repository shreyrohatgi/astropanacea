# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
import os
from .models import HomePage

# Create your views here.


def loadHomePage(request):
    HomeDetails = list(HomePage.objects.all())[-1]
    path=os.path.join(os.getcwd(),'templates','siteHome.html')

    return render(
        request,
        path,
        {
            'home': HomeDetails,
        }
    )
