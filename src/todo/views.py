from django.shortcuts import render, HttpResponse, redirect

from .models import *
from .forms import *

# Create your views here.


def indexView(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'tasks': Task.objects.all(),
        'form': TaskForm(),
    }
    return render(request, 'home.html', context=context)


def updateView(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'update_task.html', context=context)


def deleteView(request, pk):
    task = Task.objects.get(id=pk)

    if request:
        task.delete()
        return redirect('/')

    context = {'task': task, 'title': "Delete view"}
    return render(request, 'home.html', context)


def complete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request:
        task.status = True
        task.save()
        return redirect('/')

    context = {'task': task, }
    return render(request, 'home.html', context)


def uncomplete_task(request, pk):
    task = Task.objects.get(id=pk)

    if request:
        task.status = False
        task.save()
        return redirect('/')

    context = {'task': task, }
    return render(request, 'home.html', context)
