# Generated by Django 4.0.6 on 2022-07-26 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Anonymous', max_length=25)),
            ],
        ),
    ]
