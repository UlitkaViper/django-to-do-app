from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from .models import Task
from .forms import TaskForm
# Create your views here.


def delete_task(request, id):

    if request.method == 'POST':
        if 'Done' or 'Return' in request.POST:
            print(123)
            task = get_object_or_404(Task, id=id)
            # Task.objects.filter(id=id).update(completed=True)
            #task.completed = True
            task.completed = not task.completed
            task.save(update_fields=['completed'])
            # print(task)
        if 'Delete' in request.POST:
            task = get_object_or_404(Task, id=id)
            task.delete()

    return redirect('/')


class CreateTask(CreateView):
    template_name = 'task/create_task.html'
    queryset = Task.objects.all()
    form_class = TaskForm
    success_url = '/'


# class DeleteTask(DeleteView):
#     template_name = 'task/create_task.html'
#     queryset = Task.objects.all()
#     form_class = TaskForm
#     success_url = '/'


class TaskList(ListView):
    #ordering = ['-id']
    queryset = Task.objects.all().order_by('-id')
    template_name = 'task/task_list.html'
