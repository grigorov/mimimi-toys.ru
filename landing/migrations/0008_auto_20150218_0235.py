# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0007_auto_20150218_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='toy_id',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='type',
            field=models.IntegerField(default=1, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='text',
            field=models.TextField(verbose_name='Комментарий к заказу', help_text='Укажите комментарий к заказу'),
            preserve_default=True,
        ),
    ]
