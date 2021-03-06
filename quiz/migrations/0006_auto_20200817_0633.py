# Generated by Django 3.0.4 on 2020-08-17 01:03

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20200814_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 8, 17, 1, 3, 53, 939543, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question'),
        ),
    ]
