# Generated by Django 4.0.6 on 2022-07-23 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagram', '0004_alter_w_pos_alter_w_spelling'),
    ]

    operations = [
        migrations.AlterField(
            model_name='n',
            name='pos',
            field=models.CharField(default='part of speech', max_length=5),
        ),
        migrations.AlterField(
            model_name='n',
            name='spelling',
            field=models.CharField(default='spelling', max_length=100),
        ),
    ]
