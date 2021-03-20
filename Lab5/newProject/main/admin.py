from django.contrib import admin
from .models import Task, List
# Register your models here.

# admin.site.register(Task)
# admin.site.register(List)


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'dueOn', 'owner', 'mark']
    ordering = ['created', 'dueOn']
    search_fields = ['name', 'owner']
    list_filter = ['created', 'dueOn', 'mark']
    list_editable = ['mark', 'dueOn']
