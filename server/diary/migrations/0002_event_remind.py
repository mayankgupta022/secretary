# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='remind',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=True,
        ),
    ]
