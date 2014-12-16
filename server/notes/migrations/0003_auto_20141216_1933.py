# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20141215_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='board',
            name='updated',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='updated',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
