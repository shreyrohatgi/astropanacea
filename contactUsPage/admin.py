# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import QueryDetail


# Register your models here.
class QueryDetailAdmin(admin.ModelAdmin):

    list_display = ["id", "created","name" ,"emailId","query","reply","sentiment","relevant","resolved","meta"]

    class Meta:
        model = QueryDetail


admin.site.register(QueryDetail,QueryDetailAdmin)
