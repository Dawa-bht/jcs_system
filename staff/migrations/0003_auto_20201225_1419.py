# Generated by Django 3.1.2 on 2020-12-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20201224_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdetail',
            name='category',
            field=models.CharField(blank=True, choices=[('Administration', 'Administration'), ('Teaching Staff', 'Teaching Staff'), ('Supporting Staff', 'Supporting Staff')], max_length=30),
        ),
    ]