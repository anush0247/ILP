# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilpuser',
            name='Mobile',
            field=models.CharField(max_length=11, null=True, verbose_name=b'Employee Mobile No'),
        ),
    ]
