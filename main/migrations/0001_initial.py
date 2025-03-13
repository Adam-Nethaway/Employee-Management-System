# Generated by Django 5.0.6 on 2025-03-13 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('racfid', models.CharField(max_length=7, unique=True)),
                ('hours', models.IntegerField(choices=[(1, 'Full-Time'), (2, 'Part-Time')], default=1)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('position', models.IntegerField(choices=[(1, 'DCA'), (2, 'ICQA'), (3, 'Supervisor'), (4, 'Process Manager')], default=1)),
                ('team', models.IntegerField(choices=[(1, 'GUS Main Floor Putaway'), (2, 'GUS Unload'), (3, 'GUS Day Time Receiving'), (4, 'GUS Bins Receiving'), (5, 'GUS ICQA Nights'), (6, 'GUS ICQA Days')], null=True)),
                ('gear_access', models.BooleanField(default=False)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.department')),
                ('supervisor', models.ForeignKey(blank=True, limit_choices_to={'position': 3}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervisees', to='main.employee')),
            ],
        ),
        migrations.CreateModel(
            name='CorrectiveAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255)),
                ('date_issued', models.DateField(auto_now_add=True)),
                ('resolution', models.TextField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='corrective_actions', to='main.employee')),
                ('issued_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issued_corrective_actions', to='main.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Coaching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_type', models.CharField(choices=[(1, 'Recognition'), (2, 'Development')], max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coachings', to='main.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_earned', models.DateField()),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certifications', to='main.employee')),
            ],
        ),
    ]
