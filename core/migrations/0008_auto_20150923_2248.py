# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_location_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='bathroom_choices',
        ),
        migrations.RemoveField(
            model_name='location',
            name='wifi_strength',
        ),
    ]
