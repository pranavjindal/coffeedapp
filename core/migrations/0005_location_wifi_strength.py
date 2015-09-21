# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='wifi_strength',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Strong'), (1, b'Poor'), (2, b'None')]),
        ),
    ]
