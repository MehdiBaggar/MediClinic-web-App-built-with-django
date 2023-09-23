# Generated by Django 4.2.4 on 2023-08-16 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_rename_specialty_doctor_speciality'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='bio',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
    ]