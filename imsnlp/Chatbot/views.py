from django.shortcuts import render

# Create your views here.
def chitchatmodel(request):
    return render(request, 'Chatbot/index.html', {'chitchatmodel':
                                                  'Chitchatbot: Talk to me..'})

def taskedchatbot(request):
    return render(request, 'Chatbot/index.html', {'taskedchatbot':
                                                  'Taskedchatbot: How can I help?'})
def faq(request):
    return render(request, 'Chatbot/index.html', {'faq':'Any FAQ like questions..?'})
