from ast import Return
from django.shortcuts import render
from usuarios.models import Familiare
from django.http import HttpResponse
import datetime

# Create your views here.

def inicio(request):
    return render( request , "index.html")

def lista_familiare(request):
    familiare = Familiare.objects.all()
    datos = {"datos" : familiare}

    return render(request , "lista_familiare.html" , datos)

#SE DA EL ALTA DE LOS 3 FAMILIARES, SE PUEDE PASAR POR PARAMETRO 
def alta_familiare(request):
    familiar = Familiare(nombre="Jose", edad=30 , nacimiento="1988-4-15")
    familiar.save()
    familiar = Familiare(nombre="Pedro", edad=50 , nacimiento="1955-6-25")
    familiar.save()
    familiar = Familiare(nombre="Laura", edad=30 , nacimiento="1988-4-15")
    familiar.save()

    return HttpResponse("Todo ok")

