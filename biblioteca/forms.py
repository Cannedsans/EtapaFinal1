from django import forms 
from django.contrib.auth.forms import AuthenticationForm
from .models import *

class CustomAutForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Nome do usuário"}),
        label="Nome do usuário"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Senha"}),
        label="Senha"
    )

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autores
        fields = ['nome', 'sobre_nome', 'nacionalidade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-control'}),
        }
    sobre_nome = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ['titulo', 'sub_titulo', 'genero', 'sinopse', 'autor']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'sinopse': forms.Textarea(attrs={'class': 'form-control'}),
            'autor': forms.Select(attrs={'class': 'form-select'}),
        }
    sub_titulo = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sinopse = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
