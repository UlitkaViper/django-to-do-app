from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from django.views import View
from .models import Task
from .forms import TaskForm
from django.http import JsonResponse
# Create your views here.


def delete_task(request, id):

    if request.method == 'POST':
        if 'Done' in request.POST['func'] or 'Return' in request.POST['func']:
            print(123)
            print(request.POST)
            task = get_object_or_404(Task, id=id)
            # Task.objects.filter(id=id).update(completed=True)
            #task.completed = True
            task.completed = not task.completed
            task.save(update_fields=['completed'])
            return JsonResponse({'completed': task.completed}, status=200)
        if 'Delete' in request.POST['func']:
            print(321)
            task = get_object_or_404(Task, id=id)
            task.delete()
            return JsonResponse({'deleted': True}, status=200)

    return redirect('/')


class CreateTask(View):
    template_name = 'task/task_list.html'

    def get(self, request):
        queryset = Task.objects.all().order_by('-id')
        context = {'object_list': queryset}
        return render(request, 'task/task_list.html', context)

    def post(self, request):
        title = request.POST['title']

        obj = Task.objects.create(title=title)
        return JsonResponse({'title': title,
                             'id': obj.id}, status=200)


class TaskList(ListView):
    #ordering = ['-id']
    queryset = Task.objects.all().order_by('-id')
    template_name = 'task/task_list.html'
