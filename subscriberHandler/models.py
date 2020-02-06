# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class SubscriberDetail(models.Model):

    id    = models.AutoField(primary_key=True)

    created = models.DateTimeField(auto_now_add=True)
    emailId = models.TextField()
    name =  models.TextField()
    isSubscribed = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.id)


    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"
        ordering = ["-created"]

