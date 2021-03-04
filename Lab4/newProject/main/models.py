from datetime import date
from django.utils import timezone
from django.db import models

# Create your models here.


class List(models.Model):
    name = models.CharField('List', max_length=50)

    class Meta:
        verbose_name = 'List'
        verbose_name_plural = 'Lists'

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Task(models.Model):
    name = models.CharField('ToDo', max_length=250)
    created = models.DateField('Created on', default=timezone.now)
    dueOn = models.DateField('Due On', default=timezone.now)
    owner = models.CharField('Owner', max_length=50, default='admin')
    mark = models.BooleanField('Mark', default='False')
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=1)
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created': self.created,
            'dueOn': self.dueOn,
            'owner': self.owner,
            'mark': self.mark
        }






