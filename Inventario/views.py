from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext
from .forms import CreateNewClient
from .models import  TablaNueva, TablaPeliculas
# Create your views here.
# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def storage(request):
    title = 'storage'
    return render (request, 'storage.html',{
        'title' : title 
    })

def clients(request):
    
    return render(request, 'clients.html')

def movies(request):
    
    return render(request, 'movies.html')

def registration(request):
    
    return render(request, 'registration.html')

def prueba(request):
    if request.method == 'GET':
        return render(request, 'prueba.html',{'form':CreateNewClient()})
    else:
        TablaNueva.objects.create(cedula= request.POST['cedula'], name = request.POST['name'], lastName = request.POST ['lastName'] )
    return redirect ('/clients/')
    