# Generated by Django 4.0.6 on 2022-07-26 09:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_alter_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 26, 9, 16, 53, 457964, tzinfo=utc)),
        ),
    ]
