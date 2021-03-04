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

        return render(request, "registroAlumnos.html", {"form":alumnos, "mensaje": 'OK'})

    def ListarAlumnos(request):
        alumnos = Alumnos.objects.all()
        return render(request, "listarAlumnos.html", {"alumnos": alumnos})

    def edit(request, id_alumnos):
        alumno = Alumnos.objects.filter(id=id_alumnos).first()
        form = FormularioAlumnos(instance=alumno)
        return render(request, "alumnoEdit.html", {"form": form, 'alumno':alumno})

    def ActualizarAlumno(request, id_alumnos):
        alumno = Alumnos.objects.get(pk=id_alumnos)
        form = FormularioAlumnos(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            alumnos = Alumnos.objects.all()
        return render(request, "listarAlumnos.html", {"alumnos":alumnos})

    def delete(request, id_alumnos):
        alumno = Alumnos.objects.get(pk=id_alumnos)
        alumno.delete()
        alumnos = Alumnos.objects.all()
        return render(request, "listarAlumnos.html", {"alumnos": alumnos, "mensaje": 'OK'})