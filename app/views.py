from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_world(request):
    html = "<html><body><h1>Hello world!</h1></body></html>"
    return HttpResponse(html)
