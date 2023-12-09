# Generated by Django 4.2 on 2023-12-09 14:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number must be in the format +XXX-XXX-XXXX.', regex='^\\+\\d{1,3}\\d{3}\\d{3}\\d{4}$')])),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='BusTravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=255)),
                ('departure_time', models.DateTimeField()),
                ('capacity', models.IntegerField()),
                ('price', models.FloatField()),
                ('operator', models.CharField(max_length=255)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_travels', to='bus.terminal')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='originating_travels', to='bus.terminal')),
            ],
        ),
    ]