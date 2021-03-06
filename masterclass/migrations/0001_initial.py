# Generated by Django 3.2.7 on 2021-12-21 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Слог')),
                ('image', models.FileField(upload_to='images', verbose_name='Изображение')),
                ('video', models.URLField(verbose_name='Видео')),
                ('overview', models.TextField(verbose_name='Обзор')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Мастер Класс',
                'verbose_name_plural': 'Мастер Класс',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Тема',
                'verbose_name_plural': 'Тема',
                'ordering': ('title',),
            },
        ),
    ]
