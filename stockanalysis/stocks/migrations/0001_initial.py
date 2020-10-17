# Generated by Django 3.1.2 on 2020-10-17 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BSEdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copy_date', models.DateField()),
                ('security_code', models.CharField(max_length=255)),
                ('security_name', models.CharField(max_length=255)),
                ('security_group', models.CharField(max_length=255)),
                ('open', models.CharField(max_length=255)),
                ('high', models.CharField(max_length=255)),
                ('low', models.CharField(max_length=255)),
                ('close', models.CharField(max_length=255)),
                ('last', models.CharField(max_length=255)),
                ('prevclose', models.CharField(max_length=255)),
                ('no_trades', models.CharField(max_length=255)),
                ('no_of_shares', models.CharField(max_length=255)),
                ('net_turnover', models.CharField(max_length=255)),
                ('isin_code', models.CharField(max_length=288)),
            ],
        ),
    ]
