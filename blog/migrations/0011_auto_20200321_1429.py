# Generated by Django 3.0 on 2020-03-21 14:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200321_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date_post',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 21, 14, 29, 3, 881714, tzinfo=utc)),
        ),
    ]