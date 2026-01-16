from django.shortcuts import render, redirect
from .models import Todo
from .forms import TaskForm, UpdateTaskForm

def index(request):
    todos = Todo.objects.all()
    count_todos = todos.count()

    completed_todo = Todo.objects.filter(complete=True)
    count_completed_todo = completed_todo.count()

    uncompleted = count_todos - count_completed_todo

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('/')
    else:
        form = TaskForm()
    context = {
        'todos': todos,
        'form': form,
        'count_todos': count_todos,
        'count_completed_todo': count_completed_todo,
        'uncompleted': uncompleted,
    }

    return render(request, 'dashboard/index.html', context)
