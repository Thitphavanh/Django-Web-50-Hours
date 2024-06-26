# Generated by Django 5.0.2 on 2024-05-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_video_youtubevideo_video_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('published_date', models.DateField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='youtubevideo',
            options={'ordering': ['-date_created']},
        ),
    ]
