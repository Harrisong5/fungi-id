# Generated by Django 5.1 on 2024-08-15 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('id', '0005_remove_identified_image_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='identified',
            name='fungi_id',
        ),
    ]
