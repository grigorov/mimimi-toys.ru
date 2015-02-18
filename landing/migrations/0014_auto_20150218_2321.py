# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0013_auto_20150218_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(null=True, verbose_name='Email', blank=True, max_length=75, help_text='Поле обязательно для заполнения'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='mob',
            field=models.CharField(verbose_name='Телефон', null=True, max_length=12, help_text='Укажите номер телефона', default='+79000000000', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(null=True, verbose_name='Имя', blank=True, max_length=255, help_text='Укажите имя, это поле обязательное. '),
            preserve_default=True,
        ),
    ]
