# Generated by Django 5.1.4 on 2025-01-12 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_room_names'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='names',
        ),
        migrations.CreateModel(
            name='UserAttributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(default='', max_length=15)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.room')),
            ],
        ),
    ]
