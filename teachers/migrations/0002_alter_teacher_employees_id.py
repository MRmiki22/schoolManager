# Generated by Django 4.0.7 on 2023-08-11 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='employees_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.employees'),
        ),
    ]
