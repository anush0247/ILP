# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Schedule', '0001_initial'),
        ('ILP', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department_id', models.CharField(unique=True, max_length=50, verbose_name=b'Department Id')),
                ('department_name', models.CharField(max_length=50, verbose_name=b'Department Name')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guest_id', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('sessions', models.ManyToManyField(to='Schedule.Session')),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lead_id', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lg_id', models.ForeignKey(to='ILP.LG')),
                ('participant_id', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stream_id', models.CharField(unique=True, max_length=50, verbose_name=b'Stream Id')),
                ('stream_name', models.CharField(max_length=50, verbose_name=b'Stream Name')),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('designation', models.CharField(max_length=50, verbose_name=b'Designation')),
                ('department_id', models.ForeignKey(to='Users.Stream')),
                ('support_id', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lead',
            name='stream',
            field=models.ForeignKey(to='Users.Stream'),
        ),
    ]
