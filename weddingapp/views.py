from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'weddingapp/home.html', {'navbar': 'index'})

def travel(request):
    return render(request, 'weddingapp/travel.html', {'navbar': 'travel'})

