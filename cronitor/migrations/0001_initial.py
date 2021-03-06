# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 13:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.SlugField()),
                ('name', models.TextField()),
                ('auth_token', models.TextField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='log',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cronitor.Project'),
        ),
    ]
