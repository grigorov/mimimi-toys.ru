# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0010_auto_20150218_0341'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toys',
            options={'ordering': ('id',), 'verbose_name': 'Игрушки', 'verbose_name_plural': 'Игрушки'},
        ),
        migrations.AlterField(
            model_name='order',
            name='mob',
            field=phonenumber_field.modelfields.PhoneNumberField(verbose_name='Ваш номе телефона', help_text='Укажите номер телефона', max_length=12),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='text',
            field=models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True, help_text='Укажите комментарий к заказу', default='Станция метро:'),
            preserve_default=True,
        ),
    ]
