# Generated by Django 3.1.3 on 2020-12-01 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20201201_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='std_registration_form',
            name='BoarderOrDayscholar',
            field=models.CharField(blank=True, choices=[('Boarder', 'Boarder'), ('Dayscholar', 'Dayscholar')], max_length=30),
        ),
        migrations.AddField(
            model_name='std_registration_form',
            name='RegularOrRepeater',
            field=models.CharField(blank=True, choices=[('Regular', 'Regular'), ('Repeater', 'Repeater')], max_length=30),
        ),
    ]
