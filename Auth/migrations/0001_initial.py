# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ILPUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('EmpNo', models.IntegerField(unique=True, verbose_name=b'TCS Employee ID')),
                ('FirstName', models.CharField(max_length=100, verbose_name=b'First Name')),
                ('LastName', models.CharField(max_length=100, verbose_name=b'Last Name')),
                ('Email', models.EmailField(max_length=100, verbose_name=b'Employee Email Id')),
                ('DoB', models.DateField(verbose_name=b'Date of Birth')),
                ('Gender', models.CharField(max_length=1, verbose_name=b'Gender', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('Profile', models.CharField(max_length=11, verbose_name=b'Employee Profile', choices=[(b'Participant', b'Participant'), (b'Lead', b'Lead'), (b'Support', b'Support')])),
                ('is_active', models.BooleanField(default=True, verbose_name=b'Is Active User')),
                ('is_admin', models.BooleanField(default=False, verbose_name=b'Is Admin')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
