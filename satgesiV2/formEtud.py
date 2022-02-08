from django.forms import ModelForm
from .models import Stagiere
from django import forms

class StagieresForm(ModelForm):
    class Meta:
        model = Stagiere
        fields = ('matricule','NomStagiere','PrenomStagiere','niveau','DateNaissance','idf_Groupe')
        
        widgets={
            'idf Groupe': forms.TextInput(attrs={'class':'form-control','placeholder':'idf groupe'}),
            'matricule': forms.NumberInput(attrs={'class':'form-control','placeholder':'Matricule'}),
            'NomStagiere': forms.TextInput(attrs={'class':'form-control','placeholder':'Nom'}),
            'PrenomStagiere': forms.TextInput(attrs={'class':'form-control','placeholder':'Prenom'}),
            'niveau':forms.NumberInput(attrs={'class':'form-control','placeholder':'Niveau d\'etude'}),
            'DateNaissance':forms.DateInput(attrs={'class':'form-control','placeholder':'Date de naissance'}),
        }
        labels={
              'NomStagiere':'Nom',
              'PrenomStagiere' : 'Prenom',
               'niveau':'Niveau',
               'DateNaissance':'Date de niassance',
               'idf Groupe':'idf Groupe',
         }