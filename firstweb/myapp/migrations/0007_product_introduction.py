# Generated by Django 5.0.6 on 2024-06-25 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_category_alter_post_body_product_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='introduction',
            field=models.TextField(blank=True, null=True),
        ),
    ]
