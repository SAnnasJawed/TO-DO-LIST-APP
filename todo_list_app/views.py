from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .models import *
from .forms import *


# Create your views here.
def index(request):
    Todos = Task.objects.all()
    TodoForm = TodosForm()

    if request.method == 'POST':
        TodoForm = TodosForm(request.POST)
        if TodoForm.is_valid():
            TodoForm.save()
            return redirect('/')

    context = {'Todos': Todos, 'TodoForm': TodoForm}
    return render(request, 'tasks/list.html', context)


def updateTasks(request, pk):
    Todos = Task.objects.get(id=pk)
    TodoForm = TodosForm(instance=Todos)
    if request.method == 'POST':
        TodoForm = TodosForm(request.POST, instance=Todos)
        if TodoForm.is_valid():
            TodoForm.save()
            return redirect('/')

    context = {'TodoForm': TodoForm}

    return render(request, 'tasks/update_tasks.html', context)


def deleteTasks(request, pk):
    todoItem = Task.objects.get(id=pk)
    if request.method == 'POST':
        todoItem.delete()
        return redirect('/')

    context = {'todoItem': todoItem}

    return render(request, 'tasks/delete_tasks.html', context)

