# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-08 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('QuoraHandler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuoraPage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.IntegerField(default=0)),
                ('description', markdownx.models.MarkdownxField()),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'QuoraPage',
                'verbose_name_plural': 'Quora Page',
            },
        ),
    ]
