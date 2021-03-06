# Generated by Django 3.0.4 on 2020-08-13 01:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='marks',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 8, 13, 1, 7, 17, 501651, tzinfo=utc), verbose_name='date published'),
        ),
    ]
