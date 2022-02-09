from django.forms import ModelForm
from django import forms
from .models import Sinscrit

class SinscritForm(ModelForm):
    class Meta:
        model = Sinscrit
        fields = '__all__'

        widgets={
            'Type-Stage' : forms.TextInput(attrs={'class':'form-control'}),
            'idf-Groupe' : forms.TextInput(attrs={'class':'form-control'}),
         }

        labels={
            'TypeStage': 'Idf stage',

         }