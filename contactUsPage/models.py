# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class QueryDetail(models.Model):

    id    = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    emailId = models.TextField()
    name =  models.TextField()
    query = models.TextField()
    reply = models.TextField(default="")
    resolved = models.BooleanField(default=False)
    relevant = models.BooleanField(default=True)
    sentiment = models.TextField(default="")
    meta = models.TextField(default="")

    def __unicode__(self):
        return str(self.id)


    class Meta:
        verbose_name = "User Query"
        verbose_name_plural = "User Queries"
        ordering = ["-created"]
