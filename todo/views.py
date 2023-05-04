from django.shortcuts import render, redirect

from todo.forms import AddTodoForm
from todo.models import Todo


def index(request):

    if request.method == 'POST':
        form = AddTodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddTodoForm()

    todos = Todo.objects.all()
    context = {
        'todos': todos,
        'form': form,
    }
    return render(request=request, template_name='todo/index.html', context=context)


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True if todo.complete is False else False
    todo.save()
    return redirect('index')


def deleteComplete(request):
    Todo.objects.filter(complete=True).delete()
    return redirect('index')


def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')

