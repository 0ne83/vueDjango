# Generated by Django 4.2.4 on 2023-08-31 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200826_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu_question',
            name='choice',
            field=models.CharField(default='A', max_length=3),
        ),
    ]
