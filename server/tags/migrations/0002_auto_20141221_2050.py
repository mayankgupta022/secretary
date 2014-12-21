# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daytag',
            old_name='dayId',
            new_name='day',
        ),
        migrations.RenameField(
            model_name='eventtag',
            old_name='eventId',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='notetag',
            old_name='noteId',
            new_name='note',
        ),
        migrations.RenameField(
            model_name='pagetag',
            old_name='pageId',
            new_name='page',
        ),
    ]
