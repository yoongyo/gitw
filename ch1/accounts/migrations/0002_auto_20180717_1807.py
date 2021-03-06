# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-17 09:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='birth',
            field=models.DateField(default='1999-04-21'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='emergency',
            field=models.CharField(default='', max_length=20, validators=[django.core.validators.RegexValidator('^010[1-9]\\d{7}$')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='interest',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='introduce',
            field=models.CharField(default='', max_length=600),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='kakaoID',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='major',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='language',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='nextCountry',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Next', to='accounts.Country'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='visitedCountry',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Visited', to='accounts.Country'),
            preserve_default=False,
        ),
    ]
