# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_auto_20141221_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daytag',
            name='entities',
            field=models.ManyToManyField(related_name='tags', to='diary.Day'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eventtag',
            name='entities',
            field=models.ManyToManyField(related_name='tags', to='diary.Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notetag',
            name='entities',
            field=models.ManyToManyField(related_name='tags', to='notes.Note'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagetag',
            name='entities',
            field=models.ManyToManyField(related_name='tags', to='pages.Page'),
            preserve_default=True,
        ),
    ]
