# Generated by Django 4.2 on 2023-12-08 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_alter_airport_address_alter_airport_close_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='close_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='airport',
            name='open_time',
            field=models.TimeField(),
        ),
    ]
