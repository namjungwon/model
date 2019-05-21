from django.shortcuts import render, redirect
from .models import Blog
from .models import Save

def submit(request):
    s = Save()
    s.saving = request.GET['saving']
    s.save()
    return redirect('/')

def home(request):
    blogs = Blog.objects #query set #method
    return render(request, 'home.html', {'blogs':blogs})

def write(request):
    writes = Blog.objects #query set #method
    return render(request, 'write.html', {'writes':writes})

