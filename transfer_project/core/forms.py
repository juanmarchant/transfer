from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput
from .models import *

class ClienteForm(forms.Form):
    rut = forms.CharField(
        max_length=50, 
        label='RUT', 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Ingrese su RUT'
        })
    )

class ChoferSignUpForm(UserCreationForm):
    class Meta:
        model = Chofer
        fields = ['username', 'password1', 'password2', 'nombre', 'apellido', 'rut', 'patente', 'posicion']
        labels ={
            'username': 'Nombre de usuario', 
            'password1': 'Password', 
            'password2': 'Confirmar Password', 
            'nombre': 'Nombre', 
            'apellido': 'Apellido', 
            'rut': 'Rut', 
            'patente': 'Patente', 
            'posicion': 'Posicion'
        }

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'patente': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'posicion': forms.NumberInput(
                attrs={
                    'class': 'form-control ',
                }
            ),
            
        }
    def __init__(self, *args, **kwargs):
        super(ChoferSignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control'})
