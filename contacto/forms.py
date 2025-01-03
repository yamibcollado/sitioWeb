from django import forms

class Formulario(forms.Form):
    nombre=forms.CharField(label="nombre", required=True)
    email=forms.CharField(label="email", required=True)
    mensaje=forms.CharField(label="mensaje", widget=forms.Textarea)