# Generated by Django 4.1.5 on 2023-04-19 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='banners/')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Banners',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('image', models.ImageField(upload_to='categories/')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='foods/')),
                ('price', models.PositiveIntegerField(default=0)),
                ('stars', models.PositiveSmallIntegerField(default=0)),
                ('discount', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Foods',
            },
        ),
    ]
