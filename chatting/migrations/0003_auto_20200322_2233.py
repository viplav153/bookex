# Generated by Django 2.1.5 on 2020-03-22 17:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0002_auto_20200322_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 22, 17, 3, 37, 284469, tzinfo=utc)),
        ),
    ]