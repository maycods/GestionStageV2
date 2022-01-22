from django.forms import ModelForm
from .models import Type
from django import forms


class TypeForm(ModelForm):
     class Meta:
        model = Type
        fields='__all__'

        widget={
            'Type_Stage':forms.TextInput(attrs={'class':'form-control'}),
            'DateDebut':forms.DateInput(attrs={'class':'form-control'}),
            'DateFin':forms.DateInput(attrs={'class':'form-control'}),
            'NbreStagiare':forms.NumberInput(attrs={'class':'form-control'}),
            'idfGroupe':forms.TextInput(attrs={'class':'form-control'}),
         }
        labels={
              'DateDebut':'Date debut du stage',
              'DateFin':'Date fin du stage',
              'NbreStagiare':'Nombre de stagiere',
              'idfGroupe':'identificateur du groupe',
         }

