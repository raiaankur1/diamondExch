# Generated by Django 4.2.2 on 2023-07-08 09:52

import datetime
import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('diamond', '0006_depositstatement_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verifyotp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, validators=[django.core.validators.RegexValidator('^(\\+91[\\-\\s]?)?[0]?(91)?[789]\\d{9}$', 'Invalid Phone Number')])),
                ('otp', models.CharField(max_length=6)),
                ('uid', models.CharField(default='<function uuid4 at 0x0000023CA3B99160>', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 8, 15, 22, 19, 868459)),
        ),
    ]
