from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse



# Create your views here.
def console(request):
    
    context = { }
    return render(request, 'javascript/console.html', context)       

def events(request):
    
    context = { }
    return render(request, 'javascript/events.html', context)       


def traverse(request):
    
    context = { }
    return render(request, 'javascript/traverse.html', context)       
