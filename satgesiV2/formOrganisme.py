from django.forms import ModelForm
from .models import OrganismeAcceuil
from django import forms

class OrganismeAcceuilForm(ModelForm):
    class Meta:
        model = OrganismeAcceuil
        fields = '__all__'

        widgets={
            'nomOrganisme':forms.TextInput(attrs={'class':'form-control'}),
            'adresse':forms.TextInput(attrs={'class':'form-control'}),
            'RaisonSocial':forms.TextInput(attrs={'class':'form-control'}),
            'Service':forms.TextInput(attrs={'class':'form-control'}),
            'Departement':forms.TextInput(attrs={'class':'form-control'}),
        }