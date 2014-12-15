# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='attr1',
            field=models.CharField(max_length=300, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='board',
            name='attr2',
            field=models.CharField(max_length=300, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='attr1',
            field=models.CharField(max_length=300, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='note',
            name='attr2',
            field=models.CharField(max_length=300, blank=True),
            preserve_default=True,
        ),
    ]
