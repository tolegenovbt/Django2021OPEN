from django.urls import path
from main.views import todo_list, todo_list_details, completed_todo_list

urlpatterns = [
    path('todos/', todo_list, name='todo-lists'),
    path('todos/<int:pk>/', todo_list_details, name='todo-list-details'),
    path('todos/<int:pk>/completed/', completed_todo_list, name='todo-list-completed'),
]