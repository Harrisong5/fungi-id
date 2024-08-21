# Generated by Django 5.1 on 2024-08-21 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('id', '0008_alter_communitypost_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communitypost',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=8, default=None, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='communitypost',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=8, default=None, max_digits=12, null=True),
        ),
    ]
