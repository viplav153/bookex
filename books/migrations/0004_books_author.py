# Generated by Django 2.1.5 on 2020-03-25 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_books_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=150, null=True),
        ),
    ]