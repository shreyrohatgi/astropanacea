# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.shortcuts import render
import os
# Create your views here.
import json
from django.http import HttpResponse

from .models import QueryDetail
from django.views.decorators.csrf import csrf_exempt

def loadContactUsPage(request):

    #post = BlogPost.objects.get(pk=post_id)

    path=os.path.join(os.getcwd(), 'templates', 'contactUs_django.html')


    #print post.displayImage.url

    return render(
        request,
        path
        #{
        #    'post': post,
        #}
    )

@csrf_exempt
def addUserQuery(request):

    print("Got Here !")
    data = json.loads(request.body.decode('utf-8'))
    print("d", data)
    emailId = data["emailId"]
    name = data["name"]
    print("email", emailId)
    query =data["query"]
    queryDetail = QueryDetail(name=name, emailId=emailId,query=query)
    queryDetail.save()

    return HttpResponse({}, content_type="application/json")