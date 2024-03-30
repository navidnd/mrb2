# Generated by Django 5.0.3 on 2024-03-27 12:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_exersiseadd_delete_exersisename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repetitions', models.PositiveIntegerField()),
                ('duration', models.DurationField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.exersiseadd')),
            ],
        ),
    ]