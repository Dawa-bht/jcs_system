# Generated by Django 3.1.2 on 2020-12-25 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0029_auto_20201225_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='std_registration_form',
            name='admission_no',
            field=models.BigIntegerField(blank=True),
        ),
    ]
