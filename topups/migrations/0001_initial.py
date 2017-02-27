# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-27 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('user_id', models.BigIntegerField()),
                ('amoount', models.FloatField()),
                ('payment_type', models.CharField(max_length=3)),
                ('phone_number', models.IntegerField()),
                ('network', models.CharField(max_length=3)),
                ('voucher_code', models.CharField(max_length=12)),
            ],
        ),
    ]