from django.http import HttpResponse
from django.template.loader import get_template


class HomeView():

    def home(self):
        plantilla = get_template('index.html')
        return HttpResponse(plantilla.render())

    def alumnos(self):
        plantilla = get_template('registroAlumnos.html')
        return HttpResponse(plantilla.render())

    def temperatura(self):
        plantilla = get_template('registroTemp.html')
        return HttpResponse(plantilla.render())

    def visualizar(self):
        plantilla = get_template('visualizar.html')
        return HttpResponse(plantilla.render())