# Generated by Django 3.1.2 on 2020-12-23 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0027_auto_20201222_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='std_registration_form',
            name='Stream',
            field=models.CharField(blank=True, choices=[('General', 'General'), ('Agriculture', 'Agriculture'), ('Environmental Science', 'Environmental Science'), ('Economics', 'Economics'), ('Media', 'Media'), ('Commerce', 'Commerce'), ('Arts', 'Arts'), ('Science', 'Science')], max_length=30),
        ),
    ]
