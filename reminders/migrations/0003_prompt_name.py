# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='prompt',
            name='name',
            field=models.CharField(default='prompt', max_length=32),
            preserve_default=False,
        ),
    ]
