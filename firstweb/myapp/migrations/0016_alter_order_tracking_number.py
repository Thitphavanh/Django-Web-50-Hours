# Generated by Django 5.0.6 on 2024-07-15 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_trackingorderid_tracking_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='tracking_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
