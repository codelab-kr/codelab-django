# Generated by Django 5.0.7 on 2024-07-23 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['-created'], name='catalog_pro_created_b92f5e_idx'),
        ),
    ]
