from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class UserCreationFormEmail(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')