# Generated by Django 4.2.4 on 2023-08-17 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(default='2001-04-20'),
        ),
    ]
