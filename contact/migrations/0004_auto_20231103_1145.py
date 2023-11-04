# Generated by Django 3.2.23 on 2023-11-03 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_formdynmaic_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='category',
        ),
        migrations.AlterField(
            model_name='formdynmaic',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.contactus'),
        ),
        migrations.DeleteModel(
            name='ContactCategory',
        ),
    ]