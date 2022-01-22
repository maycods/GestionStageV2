from django.forms import ModelForm
from .models import GroupeStagiaire
from django import forms



class GroupeStagiaireFrom(ModelForm):
    class Meta:
        model=GroupeStagiaire
        fields='__all__'

        widget={
            'FicheDemande':forms.FileInput(attrs={'class':'form-control''<br>'}),
            'idfEncadreur':forms.TextInput(attrs={'class':'form-control'}),
            'idfpromoteur':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={
            'FicheDemande':'Demande de Stage',
             'idfEncadreur':'identificateur de l\'encadreur ',
              'idfpromoteur':'identificateur du promoteur',

        }
