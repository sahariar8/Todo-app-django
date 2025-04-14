from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo

# Create your views here.
def home(request):
    incompleted_tasks = Todo.objects.filter(is_completed=False).order_by('-created_at')
    completed_tasks = Todo.objects.filter(is_completed=True).order_by('-created_at')
    context = {
        'incompleted_tasks': incompleted_tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'home.html',context)

def addTask(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
    return redirect('home')

def mark_as_done(request, pk):
    task = get_object_or_404(Todo,id=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Todo,id=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

   
def editTask(request, pk):
    task = get_object_or_404(Todo,id=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            task.title = title
            task.save()
            return redirect('home')
    else:
        context = {
            'task': task,
            }
        return render(request, 'edit_task.html', context)
            

def deleteTask(request, pk):
    task = Todo.objects.get(Todo,id=pk)
    task.delete()
    return redirect('home')
