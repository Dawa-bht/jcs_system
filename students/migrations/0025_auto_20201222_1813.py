# Generated by Django 3.1.2 on 2020-12-22 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0024_charactercertificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactercertificate',
            name='Category',
            field=models.CharField(choices=[('Special_Recognation', 'Special_Recognation'), ('Volunteerism', 'Volunteerism'), ('Academic', 'Academic'), ('Games and Sports', 'Games and Sports'), ('Literary', 'Literary'), ('Cultural', 'Cultural')], max_length=30),
        ),
    ]