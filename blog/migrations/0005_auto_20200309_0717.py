# Generated by Django 3.0 on 2020-03-09 07:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200308_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='reply_to',
        ),
        migrations.AlterField(
            model_name='posts',
            name='date_post',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 9, 7, 17, 18, 104173, tzinfo=utc)),
        ),
    ]
