# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 04:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('privacyLevel', models.IntegerField(choices=[(0, b'Public'), (1, b'Friends'), (2, b'Friends of friends'), (3, b'Private message'), (4, b'Private')], default=0)),
                ('publishDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.Author')),
            ],
        ),
    ]
