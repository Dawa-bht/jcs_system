# Generated by Django 3.1.2 on 2020-12-25 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20201225_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdetail',
            name='category',
            field=models.CharField(blank=True, choices=[('Administration', 'Administration'), ('Teaching Staff', 'Teaching Staff'), ('Non Teaching Staff', 'Non Teaching Staff'), ('Supporting Staff', 'Supporting Staff')], max_length=30),
        ),
    ]
