# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BlogPost#,Comment

# Register your models here.
from markdownx.admin import MarkdownxModelAdmin

MarkdownxModelAdmin.list_display=["id", "created", "updated", "author", "publish",'title',"post"]

admin.site.register(BlogPost, MarkdownxModelAdmin)



"""
class CommentAdmin(admin.ModelAdmin):

    list_display = ["postId", "author", "text", "author", "created_date",'approved_comment']

    class Meta:
        model = Comment


admin.site.register(Comment,CommentAdmin)
"""


