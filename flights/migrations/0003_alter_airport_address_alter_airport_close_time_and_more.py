# Generated by Django 4.2 on 2023-12-08 13:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_airport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='airport',
            name='close_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='airport',
            name='open_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='airport',
            name='phone_number',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number must be in the format +XXX-XXX-XXXX.', regex='^\\+\\d{1,3}\\d{3}\\d{3}\\d{4}$')]),
        ),
    ]
