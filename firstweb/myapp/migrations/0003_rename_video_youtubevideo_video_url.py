# Generated by Django 5.0.2 on 2024-04-23 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_youtubevideo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtubevideo',
            old_name='video',
            new_name='video_url',
        ),
    ]
