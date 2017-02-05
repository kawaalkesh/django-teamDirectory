# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 02:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=2000)),
                ('slug', models.SlugField(blank=True, max_length=40)),
                ('responsibilities', models.CharField(default=b'', max_length=1000)),
                ('bio', models.CharField(default=b'', max_length=1000)),
                ('twitter', models.CharField(blank=True, max_length=40)),
                ('facebook', models.CharField(blank=True, max_length=40)),
                ('birthday', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
