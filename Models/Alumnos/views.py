from django.http import HttpRequest
from django.shortcuts import render

from Models.Alumnos.forms import FormularioAlumnos


class FormularioAlumnosView(HttpRequest):
    def index(request):
        Alumnos = FormularioAlumnos()
        return render(request, "registroAlumnos.html", {"form":Alumnos})

    def ProcesarFormulario(request):
        Alumnos = FormularioAlumnos(request.POST)
        if Alumnos.is_valid():
            Alumnos.save()
            Alumnos = FormularioAlumnos()

        return render(request, "registroAlumnos.html", {"form":Alumnos, "mensaje": 'Okay guardado'})