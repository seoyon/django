from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from app.models import *
from app.forms import *

# Create your views here.

def hello_world(request):
    return render(request, 'hello_world.html')

@csrf_protect
def main_page(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            content = form.cleaned_data['content']
            Comment(name = name, content = content).save()
            return HttpResponseRedirect('/')
    else:
        form = CommentForm()
    comments = Comment.objects.order_by('date')
    var = {
        'comments': comments,
        'form': form,
    }
    return render(request, 'home.html', var)
