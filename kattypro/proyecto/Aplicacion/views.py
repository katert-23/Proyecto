from django.shortcuts import render,HttpResponse,redirect
from .models import Ventas, Usuario
from .forms import Musiform
#from django.http.response import HttpResponse 

# Create your views here.


def index (request):
    inici= Ventas.objects.all()
    return render (request,"index.html", {'index': inici})

def eliminar (request,id):
    ferreteria= Ventas.objects.get(id=id)
    ferreteria.delete()
    return redirect ('index')
def Home (request):
    return render(request,"home.html")

def servicios  (request):
    return  render(request,"Servicio.html")

def ropa(request):
    return  render(request,"ropa.html")

def registrate (request):
    return  render(request,"Registrate.html")

def base (request):
    return  render(request,"base.html")


def foto (request):
    return render (request,"foto.html")

#def descarga (request):
    #return HttpResponse(directDownloadLink)

def crear (request):
    formulario = Musiform(request.POST or None , request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect ('index')
    return render (request,"crear.html", {'formulario': formulario})

def editar (request,id):
    ferreteria=Ventas.objects.get(id=id)
    formulario=Musiform(request.POST or None , request.FILES or None ,instance=ferreteria)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect ('index')
    return render (request,"editar.html", {'formulario': formulario})




