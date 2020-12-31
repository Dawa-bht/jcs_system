# Generated by Django 3.1.3 on 2020-12-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_std_registration_form_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='std_registration_form',
            name='CID',
            field=models.CharField(blank=True, default='124', max_length=11),
        ),
        migrations.AddField(
            model_name='std_registration_form',
            name='admission_no',
            field=models.IntegerField(blank=True, default='2345'),
        ),
        migrations.AddField(
            model_name='std_registration_form',
            name='date_of_admission_in_this_school',
            field=models.DateField(blank=True, default='2000-09-07'),
        ),
    ]
