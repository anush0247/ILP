# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('batch_id', models.CharField(unique=True, max_length=50, verbose_name=b'Batch Id')),
                ('batch_name', models.CharField(max_length=50, verbose_name=b'Batch Name')),
                ('start_date', models.DateField(verbose_name=b'Start Date')),
                ('end_date', models.DateField(verbose_name=b'End Date')),
            ],
        ),
        migrations.CreateModel(
            name='LearningCampus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('campus_id', models.CharField(unique=True, max_length=50, verbose_name=b'Learing Campus Id')),
                ('campus_name', models.CharField(max_length=50, verbose_name=b'Learing Campus Name')),
            ],
        ),
        migrations.CreateModel(
            name='LearningCenter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('center_id', models.CharField(unique=True, max_length=50, verbose_name=b'Learing Center Id')),
                ('center_name', models.CharField(max_length=50, verbose_name=b'Learing Center Name')),
            ],
        ),
        migrations.CreateModel(
            name='LearningRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_id', models.CharField(unique=True, max_length=50, verbose_name=b'Learing Room Id')),
                ('room_name', models.CharField(max_length=50, verbose_name=b'Learing Room Name')),
                ('room_location', models.ForeignKey(to='ILP.LearningCampus')),
            ],
        ),
        migrations.CreateModel(
            name='LG',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lg_id', models.CharField(unique=True, max_length=50, verbose_name=b'Learing Group Id')),
                ('lg_name', models.CharField(max_length=50, verbose_name=b'Learing Group Name')),
                ('batch_id', models.ForeignKey(to='ILP.Batch')),
                ('room_id', models.ForeignKey(to='ILP.LearningRoom')),
            ],
        ),
        migrations.CreateModel(
            name='LG_Lead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(verbose_name=b'Start Date')),
                ('end_date', models.DateField(verbose_name=b'End Date')),
                ('lead_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('lg_id', models.ForeignKey(to='ILP.LG')),
            ],
        ),
        migrations.AddField(
            model_name='learningcampus',
            name='center',
            field=models.ForeignKey(to='ILP.LearningCenter'),
        ),
        migrations.AddField(
            model_name='batch',
            name='center',
            field=models.ForeignKey(to='ILP.LearningCenter'),
        ),
    ]
