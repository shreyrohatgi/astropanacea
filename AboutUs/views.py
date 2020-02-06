# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import os
# Create your views here.
from AboutUs.models import Team

def aboutUs(request):

    #post = BlogPost.objects.get(pk=post_id)

    TeamMembers=Team.objects.Active()

    #print "Hello"
    #for elem in posts:
    #    print elem

    path=os.path.join(os.getcwd(), 'templates', 'aboutUs_django.html')


    #print post.displayImage.url

    return render(
        request,
        path,
        {
            'Team': TeamMembers,
        }
    )