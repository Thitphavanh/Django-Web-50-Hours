# Generated by Django 5.0.6 on 2024-07-15 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_rename_trackingorder_trackingorderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackingorderid',
            name='tracking_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_id', to='myapp.order'),
        ),
    ]
