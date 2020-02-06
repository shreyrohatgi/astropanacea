from django.db import models
from django.http import HttpResponse
# Create your models here.
from .models import SubscriberDetail

from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def addSubscriber(request):
    print("Got Here !")

    data = json.loads(request.body.decode('utf-8'))
    print("d",data)
    emailId= data["emailId"]
    name =data["name"]
    print("email",emailId)
    similarEmailIdPeople =SubscriberDetail.objects.filter(emailId=emailId)
    for id in similarEmailIdPeople:
        print(id.name,id.emailId)

    if not similarEmailIdPeople:
        subscriber = SubscriberDetail(name=name,emailId=emailId)
        subscriber.save()

    return HttpResponse({},content_type="application/json")