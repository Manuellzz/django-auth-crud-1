from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import CreateTaskForm
from .models import Task

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except:
                return render(request, 'signup.html',{
                    'form': UserCreationForm(),
                    'alert': 'El usuario ya existe'
                })
        return render(request, 'signup.html',{
            'form': UserCreationForm(),
            'alert': 'Las contraseñas no son iguales'
        })

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html',{
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'signin.html',{
                'form': AuthenticationForm(),
                'alert': 'El usuario o la contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('tasks')   

def change_password(request):
    if request.method == 'GET':
        return render(request,'change_password.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.user.username)
                user.set_password(request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except:
                return render(request, 'change_password.html',{
                    'alert': 'El usuario ya existe'
                })
        return render(request, 'change_password.html',{
            'alert': 'Las contraseñas no son iguales'
        })

@login_required
def tasks(request):
    task = Task.objects.filter(user=request.user, datedone__isnull=True)
    
    return render(request,'tasks/tasks.html',{
        'tasks': task,
        'title': 'Tareas Pendientes',
        'class': 'text-danger'
    })

@login_required
def tasks_done(request):
    task = Task.objects.filter(user=request.user, datedone__isnull=False)
    
    return render(request,'tasks/tasks.html',{
        'tasks': task,
        'title': 'Tareas Completadas',
        'class': 'text-success'
    })

@login_required
def create_tasks(request):
    try:
        if request.method == 'GET':
            return render(request,'tasks/create_tasks.html',{
                'form': CreateTaskForm()
            })
        else:
            form = CreateTaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
    except ValueError:
        return render(request,'tasks/create_tasks.html',{
            'form': CreateTaskForm(),
            'alert': 'Los datos son invalidos'
        })

@login_required
def task_detail(request,task_id):
        if request.method == 'GET':
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = CreateTaskForm(instance=task)
            return render(request,'tasks/task_detail.html',{
                'task': task,
                'form': form,
            })
        else:
            try:
                task = get_object_or_404(Task, pk=task_id, user=request.user)
                form = CreateTaskForm(request.POST, instance=task)
                form.save()
                return redirect('tasks')
            except ValueError:
                return render(request,'tasks/task_detail.html',{
                    'task': task,
                    'form': form,
                    'alert': 'Los datos son invalidos'
                })

@login_required
def complete_task(request,task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    task.datedone = timezone.now()
    task.save()
    return redirect('tasks')

@login_required
def delete_task(request,task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    task.delete()
    return redirect('tasks')