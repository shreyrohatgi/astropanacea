# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-20 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriberHandler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriberdetail',
            name='emailId',
            field=models.TextField(),
        ),
    ]
