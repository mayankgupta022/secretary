# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20141217_1933'),
        ('pages', '0002_auto_20141218_1822'),
        ('diary', '0003_auto_20141219_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField(default=0, max_length=10)),
                ('attr1', models.CharField(max_length=300, blank=True)),
                ('attr2', models.CharField(max_length=300, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('dayId', models.ManyToManyField(to='diary.Day')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField(default=0, max_length=10)),
                ('attr1', models.CharField(max_length=300, blank=True)),
                ('attr2', models.CharField(max_length=300, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('eventId', models.ManyToManyField(to='diary.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NoteTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField(default=0, max_length=10)),
                ('attr1', models.CharField(max_length=300, blank=True)),
                ('attr2', models.CharField(max_length=300, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('noteId', models.ManyToManyField(to='notes.Note')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField(default=0, max_length=10)),
                ('attr1', models.CharField(max_length=300, blank=True)),
                ('attr2', models.CharField(max_length=300, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pageId', models.ManyToManyField(to='pages.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
