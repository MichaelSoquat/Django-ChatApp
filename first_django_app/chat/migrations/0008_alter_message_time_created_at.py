# Generated by Django 4.0.4 on 2022-05-03 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_message_time_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time_created_at',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]