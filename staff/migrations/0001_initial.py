# Generated by Django 3.1.2 on 2020-12-24 06:34

from django.db import migrations, models
import students.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffDetails',
            fields=[
                ('Employee_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=30)),
                ('date_of_birth', models.DateField(blank=True)),
                ('CID', models.CharField(blank=True, max_length=11, unique=True, validators=[students.validators.validate_cid])),
                ('category', models.CharField(blank=True, choices=[('Administration', 'Administration'), ('Teaching_staff', 'Teaching_staff'), ('Supporting_staff', 'Supporting_staff')], max_length=30)),
                ('position_title', models.CharField(blank=True, max_length=50)),
                ('position_level', models.CharField(blank=True, max_length=10)),
                ('grade', models.CharField(blank=True, max_length=5)),
                ('appointment_date', models.DateField(blank=True)),
                ('joining_date_of_present_school', models.DateField(blank=True)),
                ('transfered_from', models.CharField(blank=True, max_length=50)),
                ('Employment_type', models.CharField(blank=True, choices=[('Regular', 'Regular'), ('Contract', 'Contract')], max_length=30)),
                ('nationality', models.CharField(blank=True, max_length=50)),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('qualification', models.TextField(blank=True)),
                ('contact_number', models.CharField(blank=True, max_length=8, validators=[students.validators.validate_phone])),
                ('email', models.EmailField(blank=True, max_length=254, validators=[students.validators.validate_email])),
                ('permanent_address', models.TextField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, default='/static/images/user.jpg', null=True, upload_to='images/staff')),
            ],
        ),
    ]
