import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.

def index(request):
    return HttpResponse("Welcome at my Blog Page :) ")

def posts(request):
    if request.method == "POST":
        form = request.POST
        b = BlogPost(title=form['title'], content=form['content'], time_created=datetime.datetime.now())
        b.save()
    posts = BlogPost.objects.all()
    context = {'posts':posts}
    return render(request, 'BlogPost/index.html', context)
