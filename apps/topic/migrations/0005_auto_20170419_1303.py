# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 13:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topic', '0004_auto_20170419_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topiccommentmodel',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='topicmodel',
            name='author_id',
        ),
        migrations.AddField(
            model_name='topiccommentmodel',
            name='author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='topicmodel',
            name='author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
