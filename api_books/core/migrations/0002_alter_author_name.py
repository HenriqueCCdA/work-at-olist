# Generated by Django 4.0.6 on 2022-07-20 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=120, unique=True, verbose_name='Nome'),
        ),
    ]