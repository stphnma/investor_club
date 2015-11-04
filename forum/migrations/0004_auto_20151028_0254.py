# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_remove_idea_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=100000)),
                ('author', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='IdeaPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('company', models.CharField(max_length=60)),
                ('description', models.TextField(max_length=100000)),
                ('author', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Idea',
        ),
        migrations.AddField(
            model_name='comment',
            name='idea_post',
            field=models.ForeignKey(to='forum.IdeaPost'),
        ),
    ]
