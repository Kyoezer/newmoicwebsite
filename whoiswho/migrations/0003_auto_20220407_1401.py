# Generated by Django 3.0 on 2022-04-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whoiswho', '0002_auto_20220407_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='administration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('mail_id', models.EmailField(blank=True, max_length=254)),
                ('phone_no', models.IntegerField(blank=True)),
                ('profile_img', models.ImageField(blank=True, upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='finance_division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('mail_id', models.EmailField(blank=True, max_length=254)),
                ('phone_no', models.IntegerField(blank=True)),
                ('profile_img', models.ImageField(blank=True, upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='human_resource_division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('mail_id', models.EmailField(blank=True, max_length=254)),
                ('phone_no', models.IntegerField(blank=True)),
                ('profile_img', models.ImageField(blank=True, upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='ict_division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('mail_id', models.EmailField(blank=True, max_length=254)),
                ('phone_no', models.IntegerField(blank=True)),
                ('profile_img', models.ImageField(blank=True, upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='internal_audit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('mail_id', models.EmailField(blank=True, max_length=254)),
                ('phone_no', models.IntegerField(blank=True)),
                ('profile_img', models.ImageField(blank=True, upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='policy_planning_division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('mail_id', models.EmailField(blank=True, max_length=254)),
                ('phone_no', models.IntegerField(blank=True)),
                ('profile_img', models.ImageField(blank=True, upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='procurement_section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('mail_id', models.EmailField(blank=True, max_length=254)),
                ('phone_no', models.IntegerField(blank=True)),
                ('profile_img', models.ImageField(blank=True, upload_to='pics')),
            ],
        ),
        migrations.DeleteModel(
            name='staff',
        ),
    ]
