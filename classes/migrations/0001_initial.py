# Generated by Django 4.0.7 on 2023-08-11 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Class_subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classRoomId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.class_room')),
                ('subjectId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.subject')),
            ],
        ),
    ]
