# Generated by Django 4.2.2 on 2023-07-06 19:05

import datetime
import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('diamond', '0003_alter_user_created_withdrawstatement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 7, 0, 35, 50, 252832)),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, validators=[django.core.validators.RegexValidator('^(\\+91[\\-\\s]?)?[0]?(91)?[789]\\d{9}$', 'Invalid Phone Number')]),
        ),
    ]
