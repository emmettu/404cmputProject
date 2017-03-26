# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 00:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


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
                ('privacyLevel', models.IntegerField(choices=[(0, 'Public'), (1, 'Friends'), (2, 'Friends of friends'), (3, 'Private message'), (4, 'Private'), (5, 'Unlisted')], default=0)),
                ('image_url', models.TextField(blank=True)),
                ('image', models.TextField(blank=True)),
                ('image_type', models.TextField(blank=True)),
                ('title', models.CharField(blank=True, max_length=128)),
                ('source', models.URLField(blank=True)),
                ('origin', models.URLField(blank=True)),
                ('contentType', models.CharField(choices=[('text/plain', 'Plain Text'), ('text/markdown', 'Markdown')], default='text/plain', max_length=128)),
                ('description', models.CharField(blank=True, max_length=64)),
                ('categories', models.CharField(blank=True, max_length=128)),
                ('unlisted', models.BooleanField(default=False)),
                ('UID', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('apiID', models.CharField(blank=True, max_length=128)),
                ('publishDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('visibility', models.CharField(blank=True, max_length=128)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.Author')),
            ],
        ),
    ]
