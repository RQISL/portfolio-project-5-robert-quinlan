# Generated by Django 3.2.23 on 2023-11-03 19:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0007_delete_contactcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdynmaic',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]
