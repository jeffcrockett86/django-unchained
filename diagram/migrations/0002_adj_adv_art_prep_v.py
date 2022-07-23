# Generated by Django 4.0.6 on 2022-07-22 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spelling', models.CharField(max_length=100)),
                ('pos', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Adv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spelling', models.CharField(max_length=100)),
                ('pos', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spelling', models.CharField(max_length=100)),
                ('pos', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Prep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spelling', models.CharField(max_length=100)),
                ('pos', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='V',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spelling', models.CharField(max_length=100)),
                ('pos', models.CharField(max_length=5)),
            ],
        ),
    ]