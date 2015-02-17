# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0005_auto_20150215_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='toys',
            old_name='gallery',
            new_name='image_gallery',
        ),
    ]
