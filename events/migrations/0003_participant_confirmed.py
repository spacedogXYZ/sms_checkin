# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20170423_0348'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
