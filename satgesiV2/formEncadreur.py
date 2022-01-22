from django.forms import ModelForm
from .models import Encadreur
from django import forms

class EncadreurForm(ModelForm):
    class Meta:
        model = Encadreur
        fields = "__all__"

        widgets={
            'Nomncadreur':forms.TextInput(attrs={'class':'form-control','placeholder':'Nomncadreur'}),
            'PrenomEncadreur':forms.TextInput(attrs={'class':'form-control','placeholder':'PrenomEncadreur'}),
            'Telephone': forms.NumberInput(attrs={'class':'form-control','placeholder':'Telephone'}),
            'Mail':forms.EmailInput(attrs={'class':'form-control','placeholder':'Mail'}),
            'grade':forms.TextInput(attrs={'class':'form-control','placeholder':'grade'}),
            'domaineInteret':forms.TextInput(attrs={'class':'form-control','placeholder':'grade'}),
          }
        labels={
              'Nomncadreur' :'Nom',
              'PrenomEncadreur':'Prenom',
              'domaineInteret':'domaine d\'intérêt',

            }

       