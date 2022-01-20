from django.forms import ModelForm
from .models import Promoteur
from django import forms

class PromoteurForm(ModelForm):
    class Meta:
        model = Promoteur
        fields = ('NomPromoteur','PrenomPromoteur','telephone','email','FonctionOccupée','domainIntérêt','idfOrganisme','idfGroupe')
        
        widgets={
            'NomPromoteur':forms.TextInput(attrs={'class':'form-control','placeholder':'Nomncadreur'}),
            'PrenomPromoteur':forms.TextInput(attrs={'class':'form-control','placeholder':'PrenomEncadreur'}),
            'telephone': forms.NumberInput(attrs={'class':'form-control','placeholder':'Telephone'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'email@example.com'}),
            'FonctionOccupée':forms.TextInput(attrs={'class':'form-control','placeholder':'Fonction'}),
            'domaine d intérêt':forms.TextInput(attrs={'class':'form-control','placeholder':'Domaine'}),
            'idfOrganisme' : forms.TextInput(attrs={'class':'form-control'}),
            'idfGroupe' :forms.TextInput(attrs={'class':'form-control'}),
          }