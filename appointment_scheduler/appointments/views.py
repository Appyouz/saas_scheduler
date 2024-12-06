# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Business

def index(request):
    return HttpResponse("Hello, world. You're at the appointments index.")

def home(request):
    businesses = Business.objects.all()
    return render(request, 'home.html', {'businesses':businesses})
