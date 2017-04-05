# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='Email')),
                ('birth', models.DateField(null=True, verbose_name='Date of birth', blank=True)),
                ('note', models.TextField(verbose_name='How did you hear about the project?', blank=True)),
                ('zipcode', models.CharField(max_length=9, verbose_name='Zip Code', blank=True)),
                ('street', models.CharField(max_length=255, verbose_name='Address', blank=True)),
                ('street_complement', models.CharField(max_length=255, verbose_name='Complement', blank=True)),
                ('number', models.CharField(max_length=10, verbose_name='Number', blank=True)),
                ('district', models.CharField(max_length=255, verbose_name='District', blank=True)),
                ('city', models.CharField(max_length=255, verbose_name='City', blank=True)),
                ('state', models.CharField(max_length=255, verbose_name='State', blank=True)),
                ('country', models.CharField(max_length=255, verbose_name='Country', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schooling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='schooling',
            field=models.ForeignKey(verbose_name='Schooling', blank=True, to='faca_parte.Schooling', null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='select_interest',
            field=models.ForeignKey(verbose_name='Interest', blank=True, to='faca_parte.Interest', null=True),
        ),
    ]
