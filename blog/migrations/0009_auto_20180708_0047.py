# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-08 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180707_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='imageHeight',
            field=models.IntegerField(default=200),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='imageWidth',
            field=models.IntegerField(default=200),
        ),
    ]
