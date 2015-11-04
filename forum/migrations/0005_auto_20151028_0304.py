# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_auto_20151028_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AddField(
            model_name='ideapost',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
