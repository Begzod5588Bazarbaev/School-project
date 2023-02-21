from django.shortcuts import render
from .models import *

def Menu(request):
    news = NewsLine.objects.all()
    rubric_number = Klass_Name.objects.all()
    context = {
        'news':news,
        'rubric_number':rubric_number
    }
    return render(request, 'menu.html', context)

def Klas(request, rubric_id):
    klass = Klass.objects.filter(klass_name=rubric_id)
    current_rubric = Klass_Name.objects.get(id=rubric_id)
    rubric_number = Klass_Name.objects.all()
    context = {
        'klass':klass,
        'rubric_number':rubric_number,
        'current_rubric':current_rubric
    }
    return render(request, 'class.html', context)

def Our_school(request):
    news = NewsLine.objects.all()
    rubric_number = Klass_Name.objects.all()
    context = {
        'news':news,
        'rubric_number':rubric_number
    }
    return render(request, 'our_school.html', context)

def Detail(request, pk):
    news = NewsLine.objects.get(id=pk)
    rubric_number = Klass_Name.objects.all()
    context = {
        'news':news,
        'rubric_number':rubric_number
    }
    return render(request, 'detail.html', context)
