# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_location_wifi_strength'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='bathroom_choices',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
    ]
