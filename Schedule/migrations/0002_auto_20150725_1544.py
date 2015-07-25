# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='session_id',
        ),
        migrations.RemoveField(
            model_name='timeslot',
            name='slot_id',
        ),
    ]
