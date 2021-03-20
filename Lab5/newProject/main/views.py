from django.http import HttpResponse
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render
from django.views.generic import DetailView
from datetime import datetime, timedelta
from .models import Task, List
from .serializers import ListSerializerFull, ListSerializerShort, TaskSerializerFull, TaskSerializerShort

# Create your views here.


# lists = List.objects.all()
# tasks = Task.objects.all()


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.action == 'list':
            return ListSerializerShort
        elif self.action == 'retrieve':
            return ListSerializerFull
        elif self.action == 'create':
            return ListSerializerFull
        elif self.action == 'update':
            return ListSerializerFull
        elif self.action == 'destroy':
            return ListSerializerFull


class TasksByListViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TaskSerializerFull

    @action(methods=['GET'], detail=False, permission_classes=(AllowAny,))
    def tasks_by_list(self, request, pk):
        queryset = Task.objects.filter(list_id=pk)
        serializer = TaskSerializerShort(queryset, many=True)
        return Response(serializer.data)



# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     permission_classes = (AllowAny,)
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return TaskSerializerShort
#         elif self.action == 'retrieve':
#             return TaskSerializerFull
#         elif self.action == 'create':
#             return TaskSerializerFull
#         elif self.action == 'update':
#             return TaskSerializerFull
#         elif self.action == 'destroy':
#             return TaskSerializerFull


class CompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TaskSerializerShort

    @action(methods=['GET'], detail=False, permission_classes=(AllowAny,))
    def completed_tasks(self, request, pk):
        queryset = Task.objects.filter(list_id=pk).filter(mark=True)
        serializer = TaskSerializerShort(queryset, many=True)
        return Response(serializer.data)


# class ListApiView(generics.RetrieveAPIView):
#     queryset = List.objects.all()
#     serializer_class = ListSerializerFull


# def todo_list(request):
#     list = lists
#     return render(request, 'main/todo_list.html', {'lists': list})
#
#
# def todo_list_details(request, pk):
#     task = tasks.filter(list_id__exact=pk).filter(mark__exact=False)
#     return render(request, 'main/completed_todo_list.html', {'tasks': task})
#
#
# def completed_todo_list(request, pk):
#     task = tasks.filter(list_id__exact=pk).filter(mark__exact=True)
#     return render(request, 'main/completed_todo_list.html', {'tasks': task})



