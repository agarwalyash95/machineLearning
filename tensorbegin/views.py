from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from . import linearRegression
from django.contrib import messages

from django.http import HttpResponse


def home(request):
    print('i m in home')
    return render(request, 'home.html')


def add_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'home.html', {'train': linearRegression.loadDataset(filename)})
    return render(request, 'core/simple_upload.html')


def calculate(request):
    if request.method == 'POST':
        print('i m in calculate')
        questions = request.POST.getlist('questions')
        messages.info(request, questions)
        return redirect('/')
