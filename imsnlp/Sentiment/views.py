from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    return HttpResponse("Hello from Stuttgart!")

def sentiment(request):
    #return HttpResponse("You invoked the sentiment functionality.")
    context = {'heading': 'You invoked the sentiment tool.'}
    #template = loader.get_template('Sentiment/index.html')
    #return HttpResponse(template.render(context, request))
    return render(request, 'Sentiment/index.html', context)
