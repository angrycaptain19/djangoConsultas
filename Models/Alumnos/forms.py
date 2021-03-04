from django import forms

from Models.Alumnos.models import Alumnos


class FormularioAlumnos(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = '__all__'
