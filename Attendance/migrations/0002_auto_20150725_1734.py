# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancelog',
            name='ended_at',
            field=models.TimeField(null=True, verbose_name=b'Time Slot End Time'),
        ),
    ]
