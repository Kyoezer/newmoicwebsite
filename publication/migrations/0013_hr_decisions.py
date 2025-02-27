# Generated by Django 3.0 on 2022-05-04 04:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0012_auto_20220426_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='hr_decisions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(blank=True)),
                ('SI_No', models.IntegerField(blank=True)),
                ('title', models.CharField(blank=True, max_length=400)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='files')),
            ],
        ),
    ]
