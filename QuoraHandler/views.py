# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.




from django.shortcuts import render

import os
# Create your views here.
from .models import QuoraFeed,QuoraPage

def loadAllQuora(request):

    #post = BlogPost.objects.get(pk=post_id)

    posts=QuoraFeed.objects.Published()
    pageDetails=list(QuoraPage.objects.all())[-1]


    path=os.path.join(os.getcwd(), 'templates', 'quoraPage.html')


    #print post.displayImage.url

    return render(
        request,
        path,
        {
            'posts': posts,
            'pageDetails':pageDetails
        }
    )
