# Generated by Django 5.0.3 on 2024-04-19 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_normaluser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NormalUser',
        ),
    ]