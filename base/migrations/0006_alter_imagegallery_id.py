# Generated by Django 3.2 on 2022-09-15 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20220914_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagegallery',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
