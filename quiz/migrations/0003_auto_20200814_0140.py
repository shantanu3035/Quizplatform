# Generated by Django 3.0.4 on 2020-08-13 20:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20200813_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 8, 13, 20, 10, 9, 544690, tzinfo=utc), verbose_name='date published'),
        ),
    ]