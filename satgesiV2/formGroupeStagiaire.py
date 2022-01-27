from django.forms import ModelForm
from .models import GroupeStagiaire
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    idfpromoteur = forms.ChoiceField()
    idfEncadreur = forms.ChoiceField
    file = forms.FileField()

class GroupeStagiaireFrom(ModelForm):
   
    class Meta:
        model=GroupeStagiaire
        fields= ('idfpromoteur','idfencadreur','FicheDemande')

        widget={
            'FicheDemande':forms.FileInput(attrs={'class':'form-control'}),
            'idfEncadreur':forms.TextInput(attrs={'class':'form-control'}),
            'idfpromoteur':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={
            'FicheDemande':'Demande de Stage',
            'idfEncadreur':'identificateur de l\'encadreur ',
            'idfpromoteur':'identificateur du promoteur',

        }
     
       
