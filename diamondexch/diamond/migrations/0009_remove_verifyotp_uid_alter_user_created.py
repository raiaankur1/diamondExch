# Generated by Django 4.2.2 on 2023-07-11 18:29

import datetime
from django.db import migrations, models

#


class Migration(migrations.Migration):

    dependencies = [
        ('diamond', '0008_alter_user_created_alter_verifyotp_uid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verifyotp',
            name='uid',
        ),
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(
                default=datetime.datetime(2023, 7, 11, 23, 59, 9, 753026)),
        ),
    ]
