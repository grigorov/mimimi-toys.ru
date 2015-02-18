# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0012_order_done_is'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(help_text='Поле обязательно для заполнения', max_length=75, verbose_name='Email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='mob',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Укажите номер телефона, это поле обязательно для заполнения, максимальное кол-во цифр 12, пример: +74957777777', max_length=12, verbose_name='Ваш номе телефона'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(help_text='Укажите имя, это поле обязательное. ', max_length=255, verbose_name='Имя'),
            preserve_default=True,
        ),
    ]
