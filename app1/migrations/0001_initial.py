# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app1.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field1', app1.models.CustomField(max_length=50, value_manager=app1.models.ValueManager(values=[app1.models.Value(val=1), app1.models.Value(val=2)]))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
