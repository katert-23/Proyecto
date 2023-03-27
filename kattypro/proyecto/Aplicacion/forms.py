from django import forms
from .models import Ventas,Usuario

class Musiform (forms.ModelForm):
    class  Meta:
        model =  Ventas
        fields = '__all__'
        
class Usuariform (forms.ModelForm):
    class  Meta:
        model =  Usuario
        fields = '__all__'