# Generated by Django 4.0.6 on 2022-07-18 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.AddField(
            model_name='post',
            name='number',
            field=models.IntegerField(default=69),
        ),
    ]