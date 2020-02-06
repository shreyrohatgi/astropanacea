# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.db import models


class PostQuerySet(models.QuerySet):
    def Active(self):
        return self.filter(isActive=True).order_by('order')

class Team(models.Model):

    id    = models.AutoField(primary_key=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    defaultImage = os.path.join(os.sep, "static", "Images", "image1.jpg")
    displayImage = models.ImageField(default=defaultImage, upload_to='static/media/%Y/%m/%d')
    imageHeight = models.IntegerField(default=200)
    imageWidth = models.IntegerField(default=200)
    order = models.IntegerField(default=0)

    intro = models.TextField()
    name = models.TextField()
    designation= models.TextField()
    isActive = models.BooleanField(default=True)
    objects = PostQuerySet.as_manager()

    def __unicode__(self):
        return str(self.id)


    class Meta:
        verbose_name="Team Member"
        verbose_name_plural = "Team"
        ordering =["-created"]
