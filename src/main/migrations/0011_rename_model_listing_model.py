# Generated by Django 4.2.13 on 2024-07-08 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_brand_listing_brand_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='Model',
            new_name='model',
        ),
    ]
