# Generated by Django 3.2.7 on 2021-12-21 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('masterclass', '0002_auto_20211222_0300'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clas',
            options={'ordering': ('-created',), 'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
    ]
