# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-10 15:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magicsite', '0007_auto_20180610_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_question_set',
            name='magic_wand',
        ),
        migrations.RemoveField(
            model_name='user_question_set',
            name='question_set',
        ),
        migrations.RemoveField(
            model_name='user_question_set',
            name='user',
        ),
        migrations.AddField(
            model_name='user_mahou_shoujo',
            name='question_set',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='magicsite.Question_Set'),
        ),
        migrations.DeleteModel(
            name='User_Question_Set',
        ),
    ]