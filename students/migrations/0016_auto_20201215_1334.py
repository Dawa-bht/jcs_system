# Generated by Django 3.1.2 on 2020-12-15 07:34

from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0015_auto_20201210_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='std_registration_form',
            name='CID',
            field=models.CharField(blank=True, max_length=11, unique=True, validators=[students.validators.validate_cid]),
        ),
    ]