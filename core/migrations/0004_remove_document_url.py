# Generated by Django 3.0.8 on 2020-07-31 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200730_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='url',
        ),
    ]
