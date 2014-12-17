# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_remove_board_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='board',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
    ]
