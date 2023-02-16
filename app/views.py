from django.shortcuts import render
from .models import *

def Menu(request):
    return render(request, 'menu.html')

def Class(request):
    number = Klass_Name.all()
    context = {
        'number':number
    }
    return render(request, 'number.html', context)