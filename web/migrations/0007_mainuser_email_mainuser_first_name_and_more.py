# Generated by Django 5.0.3 on 2024-04-26 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_mainuser_options_alter_mainuser_managers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainuser',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='mainuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='mainuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='mainuser',
            name='password',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='mainuser',
            name='username',
            field=models.CharField(default='', max_length=150),
        ),
    ]
