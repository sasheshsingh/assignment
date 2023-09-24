from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView, DetailView
from rest_framework.generics import ListAPIView

from task_project.task.models import TaskModel
from task_project.task.serializer import TaskModelSerializer


class TaskListView(ListView):
    model = TaskModel
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = TaskModel
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = TaskModel
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')


class TaskUpdateView(UpdateView):
    model = TaskModel
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('task-list')


class TaskDeleteView(DeleteView):
    model = TaskModel
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')
