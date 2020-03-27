from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import information
from .models import designer,jornal

def index(request):
    return HttpResponse("<h1>Hello,This is my app</h1>")

def login(request):
    if request.method == 'POST':
        form = information(request.POST)
        if form.is_valid():
            return HttpResponse('/thanks/')
    else:
        form = information()

    return render(request, '1.html', {'form': form})

def designer_list(request):
    designer_list=designer.objects.all()
    return render(request, '2.html',locals())

def jornal_list(request):
    jornal_list=jornal.objects.all()
    return render(request, '3.html',locals())