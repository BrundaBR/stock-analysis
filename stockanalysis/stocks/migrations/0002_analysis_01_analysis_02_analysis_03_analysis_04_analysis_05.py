# Generated by Django 3.1.2 on 2020-10-20 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='analysis_01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security_name', models.CharField(max_length=233)),
            ],
        ),
        migrations.CreateModel(
            name='analysis_02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security_name', models.CharField(max_length=233)),
            ],
        ),
        migrations.CreateModel(
            name='analysis_03',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security_name', models.CharField(max_length=233)),
            ],
        ),
        migrations.CreateModel(
            name='analysis_04',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security_name', models.CharField(max_length=233)),
            ],
        ),
        migrations.CreateModel(
            name='analysis_05',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('security_name', models.CharField(max_length=233)),
            ],
        ),
    ]
