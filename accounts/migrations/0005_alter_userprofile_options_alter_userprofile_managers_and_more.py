# Generated by Django 4.2.4 on 2023-08-10 14:08

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0004_rename_user_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='password1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='password2',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='speciality',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='uid',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_profiles', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default='!omg238GlUjzcNgAE07N2BRX1HXErsMrJSdgaA4yl', max_length=128),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='specialty',
            field=models.CharField(choices=[('General Practitioner (GP) or Family Medicine Physician', 'General Practitioner (GP) or Family Medicine Physician'), ('Pediatrician', 'Pediatrician'), ('Obstetrician/Gynecologist (OB/GYN)', 'Obstetrician/Gynecologist (OB/GYN)'), ('Dermatologist', 'Dermatologist'), ('Orthopedic Surgeon', 'Orthopedic Surgeon'), ('Cardiologist', 'Cardiologist'), ('Psychiatrist', 'Psychiatrist')], default='General Practitioner (GP) or Family Medicine Physician', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_profiles', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='default_username', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=30),
        ),
    ]
