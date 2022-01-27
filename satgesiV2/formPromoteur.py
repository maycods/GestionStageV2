from django.forms import ModelForm
from .models import Promoteur
from django import forms

class PromoteurForm(ModelForm):
    class Meta:
        model = Promoteur
        fields = ('NomPromoteur','PrenomPromoteur','telephone','email','FonctionOccupée','domainIntérêt','idfOrganisme','idfGroupe')
        
        widgets={
            'NomPromoteur':forms.TextInput(attrs={'class':'form-control','placeholder':'NomPromoteur'}),
            'PrenomPromoteur':forms.TextInput(attrs={'class':'form-control','placeholder':'PrenomPromoteur'}),
            'telephone': forms.NumberInput(attrs={'class':'form-control','placeholder':'Telephone'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email@example.com'}),
            'FonctionOccupée':forms.TextInput(attrs={'class':'form-control','placeholder':'Fonction'}),
            'domainIntérêt':forms.TextInput(attrs={'class':'form-control','placeholder':'Domaine'}),
            'idf_Organisme': forms.TextInput(attrs={'class':'form-control'}),
            'idf_Groupe':forms.TextInput(attrs={'class':'form-control'}),

          }
        labels={
              'idf_Organisme':'Identificateur de l\'Organisme',
               'idf_Groupe':'Identificateur du groupe',

          }
         