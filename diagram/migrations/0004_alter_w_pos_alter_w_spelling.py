# Generated by Django 4.0.6 on 2022-07-22 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagram', '0003_w'),
    ]

    operations = [
        migrations.AlterField(
            model_name='w',
            name='pos',
            field=models.CharField(default='part of speech', max_length=5),
        ),
        migrations.AlterField(
            model_name='w',
            name='spelling',
            field=models.CharField(default='spelling', max_length=100),
        ),
    ]