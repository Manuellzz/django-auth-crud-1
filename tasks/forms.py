from django import forms
from .models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        labels = {
            'title': 'Titulo',
            'description': 'Descripción',
            'important': 'Importante'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escribe el titulo de la tarea'}),
            'description': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Escribe la descripción de la tarea'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input d-block'})
        }