# Generated by Django 5.0.5 on 2024-05-17 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0003_alter_alerts_open_date_alter_alerts_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts',
            name='open_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
