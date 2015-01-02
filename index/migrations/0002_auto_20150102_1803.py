# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solution',
            name='points',
        ),
        migrations.RemoveField(
            model_name='solution',
            name='voters',
        ),
        migrations.AddField(
            model_name='solution',
            name='explanation',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
