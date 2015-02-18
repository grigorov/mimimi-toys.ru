# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0009_auto_20150218_0335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='toy_id',
            field=models.IntegerField(verbose_name='Игрушка', blank=True, null=True),
            preserve_default=True,
        ),
    ]
