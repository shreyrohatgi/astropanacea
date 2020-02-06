# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-20 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriberDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('emailId', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name_plural': 'Subscribers',
                'verbose_name': 'Subscriber',
            },
        ),
    ]