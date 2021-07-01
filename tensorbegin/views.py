from django.shortcuts import render
import tensorflow as tf
from django.http import HttpResponse


def home(request):
    print(tf.version)
    return render(request, 'home.html', {'version': tf.version})
