# Generated by Django 5.0.6 on 2024-07-07 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_rename_book_id_post_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='verse',
        ),
    ]
