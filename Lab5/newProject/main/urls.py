from django.urls import path
from main.views import ListViewSet, TasksByListViewSet, CompletedTaskViewSet

urlpatterns = [
    # path('todos/', todo_list, name='todo-lists'),
    # path('todos/<int:pk>/', todo_list_details, name='todo-list-details'),
    # path('todos/<int:pk>/completed/', completed_todo_list, name='todo-list-completed'),
    path('todos/', ListViewSet.as_view({'get': 'list',
                                        'post': 'create'})),
    path('todos/<int:pk>/', TasksByListViewSet.as_view({'get': 'tasks_by_list',
                                                        'post': 'create',
                                                        'put': 'update',
                                                        'delete': 'destroy'})),
    path('todos/<int:pk>/completed/', CompletedTaskViewSet.as_view({'get': 'completed_tasks'}))
]