# Generated by Django 4.2.4 on 2023-08-11 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='specialty',
            new_name='speciality',
        ),
    ]
