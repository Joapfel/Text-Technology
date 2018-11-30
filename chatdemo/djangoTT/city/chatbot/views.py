from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *

# Create your views here.

def index(request):
	#return HttpResponse("You are at the Chatbot which gives you information about cities")
	return render(request, 'chatbot/index.html')

def temp(request):
	return HttpResponse("You are at the temperature now.")


def citybot(request):
	#Get the request content, give back the information
	#Population, temperature today or tomorrow
	if request.method =="POST":
		response = 'I do not understand'
		data = request.POST
		userinput = data['input'].strip().lower()
		greeting = ['hi','hello']
		if userinput in greeting:
			response = "Hi there!"
		elif userinput =="how are you?":
			response = "I'm fine, thanks!"
		elif 'stuttgart' in userinput and 'temperature' in userinput: 
			response = 'The temperature in Stuttgart today is ' + str(CityInfo.objects.filter(city='Stuttgart')[0].temp_today) + ' degree.'
		return JsonResponse({'reply': response})

	return render(request, 'chatbot/citybot.html')
