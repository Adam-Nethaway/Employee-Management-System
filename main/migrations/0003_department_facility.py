# Generated by Django 5.0.6 on 2025-03-14 05:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_facility'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='facility',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.facility'),
        ),
    ]
