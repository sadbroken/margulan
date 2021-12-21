# Generated by Django 3.2.7 on 2021-12-21 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('masterclass', '0004_alter_clas_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clas',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_created', to=settings.AUTH_USER_MODEL, verbose_name='Категория'),
        ),
    ]
