# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_auto_20141120_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroup',
            name='steward',
            field=models.ForeignKey(blank=True, to='students.Student', null=True),
            preserve_default=True,
        ),
    ]
