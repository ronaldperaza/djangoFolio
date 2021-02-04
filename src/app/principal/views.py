from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Proyecto

def inico(request):
    proyectos = Proyecto.objects.all() # regresa todos los objetpos creados en proyectos
    context = {"proyectos": proyectos}
    return render(request, "principal/index.html", context)


def trabajos(request):
    proyectos = Proyecto.objects.all() # regresa todos los objetpos creados en proyectos
    context = {"proyectos": proyectos}
    return render(request, "principal/trabajos.html", context)


def detalles(request, slug_text):
    proyecto = Proyecto.objects.filter(slug= slug_text)
    if proyecto.exists():
        proyecto = proyecto.first()
    else:
        return HttpResponse("<h1>Pagina no encontrada</h1>")
    context = {'proyecto': proyecto}

    return render(request, "principal/detalles.html", context)