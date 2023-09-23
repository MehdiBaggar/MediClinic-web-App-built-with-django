# Generated by Django 4.2.4 on 2023-08-19 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Medi', '0002_alter_patient_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('symptoms', models.TextField(blank=True, null=True)),
                ('diagnosis', models.TextField(blank=True, null=True)),
                ('consultation_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medi.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Medicament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='PrescriptionMedicament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.TextField(default='', max_length=5000)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('medicament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medi.medicament')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('consultation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Medi.consultation')),
                ('medicaments', models.ManyToManyField(blank=True, to='Medi.medicament')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Medi.patient')),
                ('prescription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Medi.prescriptionmedicament')),
            ],
        ),
        migrations.AddField(
            model_name='consultation',
            name='prescription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Medi.prescriptionmedicament'),
        ),
    ]