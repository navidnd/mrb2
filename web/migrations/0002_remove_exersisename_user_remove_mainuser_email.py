# Generated by Django 5.0.3 on 2024-03-21 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exersisename',
            name='user',
        ),
        migrations.RemoveField(
            model_name='mainuser',
            name='Email',
        ),
    ]
