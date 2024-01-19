from django import forms

class FormularioCliente(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    direccion=forms.CharField(max_length=20)
    telefono=forms.IntegerField()

class addproductform(forms.Form):
    nombre=forms.CharField(max_length=20)
    descripcion=forms.CharField(max_length=20)
    numero=forms.IntegerField()

class FormularioProveedor(forms.Form):
    nombre=forms.CharField(max_length=20)
    direccion=forms.CharField(max_length=40)
    condicion_iva=forms.CharField(max_length=40)
    cuil_cuit=forms.IntegerField()
    telefono=forms.IntegerField()