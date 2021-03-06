# Generated by Django 3.0.4 on 2020-08-12 19:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_number', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(max_length=200, unique=True)),
                ('pub_date', models.DateField(default=datetime.datetime(2020, 8, 12, 19, 52, 2, 370956, tzinfo=utc), verbose_name='date published')),
                ('subject', models.CharField(choices=[('ENG', 'English'), ('MATH', 'Maths'), ('SCI', 'Science')], max_length=4)),
                ('correct_answer_text', models.TextField(max_length=200)),
                ('class_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_id', models.IntegerField()),
                ('quizdescription', models.TextField(max_length=20)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('class_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Class')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.TextField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Question')),
            ],
        ),
    ]
