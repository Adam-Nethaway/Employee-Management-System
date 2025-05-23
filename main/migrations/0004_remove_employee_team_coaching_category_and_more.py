# Generated by Django 5.0.6 on 2025-03-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_department_facility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='team',
        ),
        migrations.AddField(
            model_name='coaching',
            name='category',
            field=models.IntegerField(choices=[(1, 'Behavior'), (2, 'Attendance'), (3, 'Safety'), (4, 'Grainger Principles')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coaching',
            name='category_type',
            field=models.IntegerField(choices=[(1, 'Recognition'), (2, 'Development')]),
        ),
    ]
