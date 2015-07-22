# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Schedule', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('started_at', models.TimeField(verbose_name=b'Time Slot Start Time')),
                ('ended_at', models.TimeField(verbose_name=b'Time Slot End Time')),
                ('extra_slot_id', models.ForeignKey(blank=True, to='Schedule.ExtraSlot', null=True)),
                ('participant_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('session_id', models.ForeignKey(blank=True, to='Schedule.Session', null=True)),
            ],
        ),
    ]
