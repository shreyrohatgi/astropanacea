# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-22 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriberHandler', '0002_auto_20180820_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriberdetail',
            name='isSubscribed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='subscriberdetail',
            name='name',
            field=models.TextField(default='Unknown'),
            preserve_default=False,
        ),
    ]
