from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request,'main/index.html',{'title':'Главная страница сайта','tasks':tasks})


def about(request):
    return render(request,'main/about.html')

def createtasks(request):
    error = ''
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверна'
    form = TaskForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request,'main/createtasks.html', context) 