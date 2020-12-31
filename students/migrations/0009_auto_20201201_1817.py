# Generated by Django 3.1.3 on 2020-12-01 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_std_registration_form_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='std_registration_form',
            name='father_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='std_registration_form',
            name='fathers_occupation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='std_registration_form',
            name='mother_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='std_registration_form',
            name='mothers_occupation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='std_registration_form',
            name='parents_mobile_number',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]