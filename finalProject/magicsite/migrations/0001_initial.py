# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-21 16:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150)),
                ('score', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Question_Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='question_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magicsite.Question_Set'),
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magicsite.Question'),
        ),
    ]
