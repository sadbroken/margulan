# Generated by Django 3.2.7 on 2021-12-21 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статья'},
        ),
    ]
