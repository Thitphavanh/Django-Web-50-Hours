# Generated by Django 5.0.6 on 2024-07-15 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_order_not_complete_order_tracking_number_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TrackingOrder',
            new_name='TrackingOrderID',
        ),
    ]
