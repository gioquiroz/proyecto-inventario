from django import forms

class CreateNewClient(forms.Form):
    cedula = forms.CharField(label="Ingrese Cedula: ")
    name = forms.CharField(label="Ingrese nombres: ")
    lastName = forms.CharField(label="Ingrese apellidos: ")

class CreateNewStorageItem(forms.Form):
    title = forms.CharField(label="Ingrese titulo de pelicula o objeto")
