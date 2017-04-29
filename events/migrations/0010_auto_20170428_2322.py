# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20170428_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='affinity_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='affinity_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='ends_at',
            field=models.DateTimeField(verbose_name='Ends at (local)'),
        ),
        migrations.AlterField(
            model_name='event',
            name='starts_at',
            field=models.DateTimeField(verbose_name='Starts at (local)'),
        ),
    ]
