# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20141216_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='parent',
        ),
    ]
