from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {}
    return render(request, 'homeapp/home.html', context)

def contact(request):
    context = {}
    return render(request, 'homeapp/contact.html', context)

def fixtures(request):
    context = {}
    return render(request, 'homeapp/fixtures.html', context)

def table(request):
    context = {}
    return render(request, 'homeapp/table.html', context)

def update(request):
    context = {}
    return render(request, 'homeapp/update.html', context)