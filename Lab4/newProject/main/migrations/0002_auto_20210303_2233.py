# Generated by Django 3.1.6 on 2021-03-03 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='dueToDate',
        ),
        migrations.AddField(
            model_name='task',
            name='dueOn',
            field=models.DateField(default=datetime.date(2021, 3, 3), verbose_name='Due On'),
        ),
        migrations.AlterField(
            model_name='task',
            name='creationDate',
            field=models.DateField(default=datetime.date(2021, 3, 3), verbose_name='Created on'),
        ),
    ]