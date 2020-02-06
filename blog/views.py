# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import os
# Create your views here.


from .models import BlogPost

def post_detail(request, post_id):

    post = BlogPost.objects.get(pk=post_id)

    path=os.path.join(os.getcwd(), 'templates', 'posts_post.html')


    print(post.displayImage.url)

    return render(
        request,
        path,
        {
            'post': post,
        }
    )