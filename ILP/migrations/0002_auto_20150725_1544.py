# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ILP', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='batch_id',
        ),
        migrations.RemoveField(
            model_name='learningcampus',
            name='campus_id',
        ),
        migrations.RemoveField(
            model_name='learningcenter',
            name='center_id',
        ),
        migrations.RemoveField(
            model_name='lg',
            name='lg_id',
        ),
    ]
