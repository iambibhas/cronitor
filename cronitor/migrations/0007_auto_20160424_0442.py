# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 23:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cronitor', '0006_auto_20160424_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
