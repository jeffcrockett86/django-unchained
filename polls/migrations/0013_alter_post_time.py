# Generated by Django 4.0.6 on 2022-07-22 23:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_alter_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 23, 4, 10, 955689, tzinfo=utc)),
        ),
    ]
