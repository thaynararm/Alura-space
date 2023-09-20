# Generated by Django 4.2.3 on 2023-08-23 02:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0002_photography_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='photography',
            name='photo_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='photography',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
