# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app1.models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20141014_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modela',
            name='field1',
            field=app1.models.CustomField(max_length=50, value_manager=app1.models.ValueManager(values=[app1.models.Value(val=1), app1.models.Value(val=2)])),
        ),
    ]
