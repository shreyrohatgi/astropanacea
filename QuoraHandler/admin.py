# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
# Register your models here.
from markdownx.admin import MarkdownxModelAdmin
from .models import QuoraFeed,QuoraPage

class MarkdownxModelAdminSub2(MarkdownxModelAdmin):
    pass

class MarkdownxModelAdminSub3(MarkdownxModelAdmin):
    pass




MarkdownxModelAdminSub2.list_display=["id", "question", "order", "code","publish"



                                  ]

admin.site.register(QuoraFeed, MarkdownxModelAdminSub2)



MarkdownxModelAdminSub3.list_display=["id", "created", "updated", "title","description"



                                  ]

admin.site.register(QuoraPage, MarkdownxModelAdminSub3)

