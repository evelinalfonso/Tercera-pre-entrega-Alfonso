from django import forms

# Create your forms here.
class ProductosFormulario(forms.Form):

    nombre= forms.CharField(max_length=40)
    precio= forms.IntegerField()
    marca = forms.CharField(max_length=40)

class ClientesFormulario(forms.Model):

    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    mail = forms.EmailField()

class ProveedoresFormulario(forms.Model):

    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    mail = forms.EmailField()
