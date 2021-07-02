from django.shortcuts import render
import tensorflow as tf
from django.http import HttpResponse


def home(request):
    tf_var = tf.ones([5, 5, 5])
    return render(request, 'home.html', {'version': tf_var , 'shape': tf_var.shape})
