# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-14 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mangaki', '0057_auto_20160702_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=128)),
                ('language', models.CharField(blank=True, db_index=True, max_length=50)),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangaki.Work')),
            ],
        ),
    ]
