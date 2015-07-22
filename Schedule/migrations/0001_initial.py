# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ILP', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraSlot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'Date')),
                ('participant_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_id', models.CharField(unique=True, max_length=50, verbose_name=b'Schedule Id')),
                ('session_name', models.CharField(max_length=50, verbose_name=b'Schedule Name')),
                ('date', models.DateField(verbose_name=b'Date')),
                ('incharge', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('lg_id', models.ForeignKey(to='ILP.LG')),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slot_id', models.CharField(unique=True, max_length=50, verbose_name=b'Time Slot  Id')),
                ('slot_name', models.CharField(max_length=50, verbose_name=b'Time Slot Name')),
                ('start_time', models.TimeField(verbose_name=b'Time Slot Start Time')),
                ('end_time', models.TimeField(verbose_name=b'Time Slot End Time')),
                ('is_break', models.BooleanField(default=False, verbose_name=b'Is a Break ?')),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='time_slot',
            field=models.ForeignKey(to='Schedule.TimeSlot'),
        ),
        migrations.AddField(
            model_name='extraslot',
            name='time_slot',
            field=models.ForeignKey(to='Schedule.TimeSlot'),
        ),
    ]
