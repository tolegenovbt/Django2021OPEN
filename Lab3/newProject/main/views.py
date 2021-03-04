from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, timedelta

# Create your views here.
def todo_list(request):
    task1 = {
        'name': 'Task1',
        'id': 1,
        'created': '10/09/2018',
        'dueOn': '12/09/2019',
        'owner': 'admin',
        'mark': 0,
    }
    task2 = {
        'name': 'Task2',
        'id': 2,
        'created': '10/09/2018',
        'dueOn': '12/09/2019',
        'owner': 'admin',
        'mark': 0,
    }
    task3 = {
        'name': 'Task3',
        'id': 3,
        'created': '10/09/2018',
        'dueOn': '12/09/2019',
        'owner': 'admin',
        'mark': 0,
    }
    task4 = {
        'name': 'Task4',
        'id': 4,
        'created': '10/09/2018',
        'dueOn': '12/09/2019',
        'owner': 'admin',
        'mark': 0,
    }
    context = {
        'tasks': [task1, task2, task3, task4],
        'id': id
    }
    return render(request, 'main/todo_list.html', context=context)

def completed_todo_list(request):
    task0 = {
        'name': 'Task0',
        'id': 0,
        'created': '10/09/2018',
        'dueOn': '12/09/2019',
        'owner': 'admin',
        'mark': 1,
    }
    task5 = {
        'name': 'Task5',
        'id': 5,
        'created': '10/09/2018',
        'dueOn': '12/09/2019',
        'owner': 'admin',
        'mark': 1,
    }
    completedTasks = {
        'tasks': [task0,task5],
    }
    return render(request, 'main/completed_todo_list.html', context=completedTasks)


