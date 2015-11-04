# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20151018_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='idea',
            name='author',
        ),
    ]
