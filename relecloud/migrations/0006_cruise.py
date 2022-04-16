# Generated by Django 4.0.4 on 2022-04-15 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relecloud', '0005_destination_slugfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cruise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=2000)),
                ('destinations', models.ManyToManyField(related_name='destinations', to='relecloud.destination')),
            ],
        ),
    ]
