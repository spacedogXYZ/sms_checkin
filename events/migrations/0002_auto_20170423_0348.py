# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 03:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='prompt_after',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='reminders.Prompt'),
        ),
        migrations.AddField(
            model_name='event',
            name='prompt_before',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='reminders.Prompt'),
        ),
    ]
