# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Team


# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    list_display = ["id", "created", "updated","isActive","name" ,"designation","displayImage","order"]

    class Meta:
        model = Team


admin.site.register(Team,TeamAdmin)


"""

id    = models.AutoField(primary_key=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    defaultImage = os.path.join(os.sep, "static", "Images", "image1.jpg")
    displayImage = models.ImageField(default=defaultImage, upload_to='static/media/%Y/%m/%d')
    imageHeight = models.IntegerField(default=200)
    imageWidth = models.IntegerField(default=200)
    
    intro = models.TextField()
    name = models.TextField()
    designation= models.TextField()

"""