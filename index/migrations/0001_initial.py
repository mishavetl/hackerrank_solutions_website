# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('source', models.TextField(default=b'')),
                ('points', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('moderator', models.ForeignKey(related_name='moderated_solutions', to=settings.AUTH_USER_MODEL)),
                ('voters', models.ManyToManyField(related_name='liked_solutions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'solutions',
            },
            bases=(models.Model,),
        ),
    ]
