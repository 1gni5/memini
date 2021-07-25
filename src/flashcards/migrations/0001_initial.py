# Generated by Django 3.2.5 on 2021-07-25 21:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
                ('repetition', models.PositiveIntegerField(default=0)),
                ('easiness_factor', models.FloatField(default=2.5)),
                ('interval', models.DurationField(default=datetime.timedelta(days=1))),
            ],
        ),
    ]
