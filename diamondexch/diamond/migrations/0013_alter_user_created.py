# Generated by Django 4.2.2 on 2023-07-21 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diamond', '0012_alter_depositstatement_utrno_alter_user_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 13, 15, 1, 622660)),
        ),
    ]
