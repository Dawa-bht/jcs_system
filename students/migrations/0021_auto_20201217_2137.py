# Generated by Django 3.1.2 on 2020-12-17 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0020_auto_20201217_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinaryissue',
            name='Student_code',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.std_registration_form'),
        ),
    ]
