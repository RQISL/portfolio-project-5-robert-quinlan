# Generated by Django 3.2.21 on 2023-10-19 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_categories_groups_friendly_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories_groups',
            new_name='CategoriesGroups',
        ),
    ]
