from django.http import HttpResponse
from django.template.loader import get_template


class HomeView():

    def home(self):
        plantilla = get_template('index.html')
        return HttpResponse(plantilla.render())

    def alumnos(self):
        plantilla = get_template('registroAlumnos.html')
        return HttpResponse(plantilla.render())
