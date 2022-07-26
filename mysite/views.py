from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Home(request):
    return render(request, 'mysite/dashboard.html')

def about(request):
    return render(request, 'mysite/about.html')

def services(request):
	return render(request, 'mysite/services.html')

def contactus(request):
	return render(request, 'mysite/contact.html')
