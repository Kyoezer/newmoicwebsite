# Generated by Django 3.0 on 2022-04-13 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoiswho', '0004_merge_20220413_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office_of_minister',
            name='phone_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
