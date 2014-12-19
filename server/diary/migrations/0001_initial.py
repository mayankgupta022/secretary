# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField(default=0, max_length=10)),
                ('active', models.IntegerField(default=0, max_length=1)),
                ('attr1', models.CharField(max_length=300, blank=True)),
                ('attr2', models.CharField(max_length=300, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=300)),
                ('date', models.DateTimeField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(blank=True)),
                ('attr1', models.CharField(max_length=300, blank=True)),
                ('attr2', models.CharField(max_length=300, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('reminder', models.DateTimeField(blank=True)),
                ('priority', models.IntegerField(default=0, max_length=10)),
                ('active', models.IntegerField(default=0, max_length=1)),
                ('attr1', models.CharField(max_length=300, blank=True)),
                ('attr2', models.CharField(max_length=300, blank=True)),
                ('desc', models.TextField(blank=True)),
                ('calender', models.ForeignKey(to='diary.Calender')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
