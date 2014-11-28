# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_auto_20141128_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='model',
            field=models.CharField(max_length=125, null=True, blank=True),
            preserve_default=True,
        ),
    ]
