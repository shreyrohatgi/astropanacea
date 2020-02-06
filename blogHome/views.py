# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import os
# Create your views here.
from blog.models import BlogPost

def loadAllPosts(request):

    #post = BlogPost.objects.get(pk=post_id)

    posts=BlogPost.objects.Published()

    print("Hello")
    for elem in posts:
        print(elem)

    path=os.path.join(os.getcwd(), 'templates', 'blogHome.html')


    #print post.displayImage.url

    return render(
        request,
        path,
        {
            'posts': posts,
        }
    )