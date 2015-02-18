# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0011_auto_20150218_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='done_is',
            field=models.CharField(choices=[('Done', 'Выполнен'), ('Undone', 'Не Выполнен')], default='Undone', verbose_name='Выполнен ли заказ?', max_length=6),
            preserve_default=True,
        ),
    ]
