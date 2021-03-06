# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0008_auto_20160610_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax_total',
            field=models.DecimalField(default=0.0, max_digits=50, decimal_places=2),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(default=0.0, max_digits=50, decimal_places=2),
        ),
    ]
