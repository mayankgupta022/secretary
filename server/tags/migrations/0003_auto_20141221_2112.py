# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_auto_20141221_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daytag',
            old_name='day',
            new_name='entities',
        ),
        migrations.RenameField(
            model_name='eventtag',
            old_name='event',
            new_name='entities',
        ),
        migrations.RenameField(
            model_name='notetag',
            old_name='note',
            new_name='entities',
        ),
        migrations.RenameField(
            model_name='pagetag',
            old_name='page',
            new_name='entities',
        ),
    ]
