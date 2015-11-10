# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20151028_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEmails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('First_Name', models.CharField(max_length=60)),
                ('Last_Name', models.CharField(max_length=60)),
                ('Email_Address', models.CharField(max_length=60)),
            ],
        ),
    ]
