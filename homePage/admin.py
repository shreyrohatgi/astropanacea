# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import HomePage

# Register your models here.
from markdownx.admin import MarkdownxModelAdmin

class MarkdownxModelAdminSub(MarkdownxModelAdmin):
    pass




MarkdownxModelAdminSub.list_display=["id", "title", "body", "defaultImage",
                                  "backGroundImage",
                                  'carousel1QuoteTitle',"carousel1Quote","carousel1Image",
                                  'carousel2QuoteTitle',"carousel2Quote","carousel2Image",
                                  'carousel3QuoteTitle',"carousel3Quote","carousel3Image"


                                  ]

admin.site.register(HomePage, MarkdownxModelAdminSub)


