# Generated by Django 2.1.5 on 2020-03-23 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chatting', '0006_auto_20200323_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 23, 10, 14, 26, 299575, tzinfo=utc)),
        ),
    ]
