# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 23:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cronitor', '0005_auto_20160424_0425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'ordering': ['-created_at']},
        ),
    ]
