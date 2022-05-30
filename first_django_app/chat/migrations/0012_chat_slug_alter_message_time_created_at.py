# Generated by Django 4.0.4 on 2022-05-29 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_chat_name_alter_message_time_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='slug',
            field=models.SlugField(default=None, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='time_created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 9, 16, 43, 537588)),
        ),
    ]