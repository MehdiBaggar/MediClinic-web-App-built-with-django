# Generated by Django 4.2.4 on 2023-08-20 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Medi', '0003_consultation_medicament_prescriptionmedicament_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='consultation',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='medicaments',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='prescription',
        ),
        migrations.RemoveField(
            model_name='prescriptionmedicament',
            name='medicament',
        ),
        migrations.DeleteModel(
            name='Consultation',
        ),
        migrations.DeleteModel(
            name='Medicament',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='PrescriptionMedicament',
        ),
    ]
