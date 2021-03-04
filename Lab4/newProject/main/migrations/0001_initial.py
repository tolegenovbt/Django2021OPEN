# Generated by Django 3.1.6 on 2021-03-03 07:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='List')),
            ],
            options={
                'verbose_name': 'List',
                'verbose_name_plural': 'Lists',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='ToDo')),
                ('creationDate', models.DateField(default=datetime.date(2021, 3, 3), verbose_name='Created at')),
                ('dueToDate', models.DateField(default=datetime.date(2021, 3, 3), verbose_name='Due To')),
                ('owner', models.CharField(default='admin', max_length=50, verbose_name='Owner')),
                ('mark', models.BooleanField(default='False', verbose_name='Mark')),
                ('list', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.list')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
