from django.http import HttpRequest
from django.shortcuts import render

from Models.Alumnos.forms import FormularioAlumnos
from Models.Alumnos.models import Alumnos

class FormularioAlumnosView(HttpRequest):
    def index(request):
        alumnos = FormularioAlumnos()
        return render(request, "registroAlumnos.html", {"form":alumnos})

    def ProcesarFormulario(request):
        alumnos = FormularioAlumnos(request.POST)
        if alumnos.is_valid():
            alumnos.save()
            alumnos = FormularioAlumnos()

        return render(request, "registroAlumnos.html", {"form":alumnos, "mensaje": 'Okay guardado'})

    def ListarAlumnos(request):
        alumnos = Alumnos.objects.all()
        return render(request, "listarAlumnos.html", {"alumnos": alumnos})
