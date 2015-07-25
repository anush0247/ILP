# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='department_id',
        ),
        migrations.RemoveField(
            model_name='stream',
            name='stream_id',
        ),
    ]
