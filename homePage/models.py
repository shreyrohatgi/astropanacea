# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.db import models
from markdownx.utils import markdownify
from markdownx.models import MarkdownxField


choiceFields= [("black","black") ,("white","white") ,("brown","brown"), ("pink","pink") ,("orange","orange"),
               ("red","red"),("gold","gold"),("green","green"),("chrome","chrome")]
class HomePage(models.Model):

    id    = models.AutoField(primary_key=True)

    ## Main
    title = models.TextField()
    titleColor = models.CharField(max_length=20, choices=choiceFields,default='white')
    body = MarkdownxField()
    bodyColor = models.CharField(max_length=20, choices=choiceFields,default='white')

    defaultImage=os.path.join(os.sep,"static","Images","image1.jpg")
    backGroundImage = models.ImageField(default=defaultImage, upload_to='static/media/%Y/%m/%d')

    ## Carousels
    carousel1QuoteTitle = models.TextField()
    carousel1QuoteTitleColor = models.CharField(max_length=20, choices=choiceFields, default='white')
    carousel1Quote = models.TextField()
    carousel1QuoteColor = models.CharField(max_length=20, choices=choiceFields, default='white')
    carousel1Image= models.ImageField(default=defaultImage,upload_to='static/media/%Y/%m/%d')



    carousel2QuoteTitle = models.TextField()
    carousel2QuoteTitleColor = models.CharField(max_length=20, choices=choiceFields, default='white')
    carousel2Quote = models.TextField()
    carousel2QuoteColor = models.CharField(max_length=20, choices=choiceFields, default='white')
    carousel2Image = models.ImageField(default=defaultImage, upload_to='static/media/%Y/%m/%d')


    carousel3QuoteTitle = models.TextField()
    carousel3QuoteTitleColor = models.CharField(max_length=20, choices=choiceFields, default='white')
    carousel3Quote = models.TextField()
    carousel3QuoteColor = models.CharField(max_length=20, choices=choiceFields, default='white')
    carousel3Image = models.ImageField(default=defaultImage, upload_to='static/media/%Y/%m/%d')





    def __unicode__(self):
        return str(self.id)

    @property
    def formatted_markdown(self):
        return markdownify(self.body)

    class Meta:
        verbose_name="Home Page"
        verbose_name_plural = "Home Page"


