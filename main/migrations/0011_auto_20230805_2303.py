# Generated by Django 3.1.13 on 2023-08-05 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20230805_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question_db',
            name='optionA',
        ),
        migrations.RemoveField(
            model_name='question_db',
            name='optionB',
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 5, 23, 3, 24, 562517)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 5, 23, 3, 24, 562493)),
        ),
    ]
