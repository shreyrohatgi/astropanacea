# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-07 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180706_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='displayImage',
            field=models.ImageField(default='/Users/vaibhavarora/Desktop/PycharmProjects/paxcelProjects/web/astropanacea/static/image1.jpg', upload_to='media/%Y/%m/%d'),
        ),
    ]
