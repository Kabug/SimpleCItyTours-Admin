# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-17 18:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_audio_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='img',
        ),
        migrations.RemoveField(
            model_name='location',
            name='isReady',
        ),
        migrations.RemoveField(
            model_name='location',
            name='visibility',
        ),
    ]