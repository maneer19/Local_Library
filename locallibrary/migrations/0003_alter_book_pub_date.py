# Generated by Django 4.2 on 2023-09-07 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locallibrary', '0002_alter_book_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 7, 11, 31, 49, 737815), verbose_name='date'),
        ),
    ]
