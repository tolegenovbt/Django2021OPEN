from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from datetime import datetime, timedelta
from .models import Task, List

# Create your views here.


lists = List.objects.all()
tasks = Task.objects.all()


def todo_list(request):
    list = lists
    return render(request, 'main/todo_list.html', {'lists': list})


def todo_list_details(request, pk):
    task = tasks.filter(list_id__exact=pk).filter(mark__exact=False)
    return render(request, 'main/completed_todo_list.html', {'tasks': task})


def completed_todo_list(request, pk):
    task = tasks.filter(list_id__exact=pk).filter(mark__exact=True)
    return render(request, 'main/completed_todo_list.html', {'tasks': task})



