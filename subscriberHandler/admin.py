from django.contrib import admin
from .models import SubscriberDetail
# Register your models here.
class SubscriberDetailAdmin(admin.ModelAdmin):

    list_display = ["id", "created","name" ,"emailId","isSubscribed"]

    class Meta:
        model = SubscriberDetail


admin.site.register(SubscriberDetail,SubscriberDetailAdmin)