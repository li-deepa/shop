# Generated by Django 4.0.4 on 2022-04-15 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0006_cruise'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='SlugField',
            new_name='slug',
        ),
    ]
