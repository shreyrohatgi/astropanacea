# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import os
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class PostQuerySet(models.QuerySet):
    def Published(self):
        return self.filter(publish=True).order_by('order')

class QuoraFeed(models.Model):

    id    = models.AutoField(primary_key=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)
    question=models.TextField()

    code =MarkdownxField()
    publish = models.BooleanField(default=True)
    objects = PostQuerySet.as_manager()

    def __unicode__(self):
        return str(self.id)

    @property
    def formatted_markdown(self):
        return markdownify(self.code)

    class Meta:
        verbose_name = "Quora Feed"
        verbose_name_plural = "Quora Feed"
        ordering = ["-created"]


class QuoraPage(models.Model):

    id    = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.TextField()
    description=MarkdownxField()
    objects = PostQuerySet.as_manager()

    def __unicode__(self):
        return str(self.id)

    @property
    def formatted_markdown(self):
        return markdownify(self.description)

    class Meta:
        verbose_name = "QuoraPage"
        verbose_name_plural = "Quora Page"
        ordering = ["-created"]

