from django.shortcuts import render
from django.http import HttpResponse

from app.models import *

# Create your views here.

def hello_world(request):
    return render(request, 'hello_world.html')

def main_page(request):
    comments = Comment.objects.order_by('date')
    var = {
        'comments': comments,
    }
    return render(request, 'home.html', var)
