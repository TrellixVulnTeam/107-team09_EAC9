# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-10 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magicsite', '0006_auto_20180607_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_question_set',
            old_name='question_Set',
            new_name='question_set',
        ),
        migrations.RemoveField(
            model_name='user_question_set',
            name='op_type',
        ),
        migrations.AddField(
            model_name='user_question_set',
            name='magic_wand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magicsite.Magic_Wand'),
        ),
    ]