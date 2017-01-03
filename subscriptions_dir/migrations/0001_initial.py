# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 00:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subscriptions_lib', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Giftee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_purchased', models.DateTimeField()),
                ('date_completed', models.DateTimeField()),
                ('giftee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions_dir.Giftee')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions_dir.PaymentMethod'),
        ),
        migrations.AddField(
            model_name='order',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions_lib.Subscription'),
        ),
    ]