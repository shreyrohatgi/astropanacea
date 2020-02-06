# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.db import models
from django import forms
from markdownx.utils import markdownify
from markdownx.models import MarkdownxField
from django.conf import settings
from taggit.managers import TaggableManager
from django.utils import timezone

Authors =[ ("Shivam","Shivam Angurala"),("Saloni","Saloni Angurala")]

class PostQuerySet(models.QuerySet):
    def Published(self):
        return self.filter(publish=True)

class BlogPost(models.Model):

    id    = models.AutoField(primary_key=True)

    useVideo = models.BooleanField(default=False)
    videoEmbedding = MarkdownxField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    defaultImage = os.path.join(os.sep, "static", "Images", "image1.jpg")
    displayImage = models.ImageField(default=defaultImage, upload_to='static/media/%Y/%m/%d')
    imageHeight = models.IntegerField(default=200)
    imageWidth = models.IntegerField(default=200)
    author = models.CharField(max_length=20,choices=Authors)
    title = models.TextField()
    publish = models.BooleanField(default=True)
    post= MarkdownxField()
    tags = TaggableManager()
    objects=PostQuerySet.as_manager()

    def __unicode__(self):
        return str(self.id)


    @property
    def formatted_markdown(self):
        return markdownify(self.post)

    @property
    def formatted_YouTube(self):
        return markdownify(self.videoEmbedding)

    class Meta:
        verbose_name="Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering =["-created"]
"""
class Comment(models.Model):
    postId = models.ForeignKey('blog.BlogPost', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
"""


"""
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
"""



