# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('parent', models.IntegerField(default=0, max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField(default=0, max_length=10)),
                ('attr1', models.CharField(max_length=300)),
                ('attr2', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('owner', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=300)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('context', models.IntegerField(default=1, max_length=2)),
                ('active', models.IntegerField(default=0, max_length=1)),
                ('priority', models.IntegerField(default=0, max_length=10)),
                ('attr1', models.CharField(max_length=300)),
                ('attr2', models.CharField(max_length=300)),
                ('content', models.TextField(blank=True)),
                ('board', models.ForeignKey(to='notes.Board')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
