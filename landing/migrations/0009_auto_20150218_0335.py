# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_auto_20150218_0235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='type',
        ),
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.IntegerField(verbose_name='Цена', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='toy_id',
            field=models.ForeignKey(to='landing.Toys', verbose_name='Игрушка', null=True, blank=True),
            preserve_default=True,
        ),
    ]
