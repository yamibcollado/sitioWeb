from django import forms

class Formulario(forms.Form):
    nombre=forms.CharField(label="nombre", required=True)
    email=forms.CharField(label="email", required=True)
    contenido=forms.CharField(label="contenido", widget=forms.Textarea)