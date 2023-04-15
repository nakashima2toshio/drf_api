from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView, DetailView, UpdateView, DeleteView
from todo_task.models import Task
from todo_task.forms import TaskForm

class TaskListView(ListView):
    model = Task
    template_name = 'todo_task/todo_task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo_task/task_create.html'
    success_url = reverse_lazy('task_list')

class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo_task/task_detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'todo_task/task_update.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo_task/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')




