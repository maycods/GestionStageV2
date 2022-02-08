from django.forms import ModelForm
from django import forms
from .models import SeDeroule

class SedrouleForm(ModelForm):
    class Meta:
        model = SeDeroule
        fields = '__all__'

        widgets={
            'Type-Stage' : forms.TextInput(attrs={'class':'form-control'}),
            'idf-Organisme' : forms.TextInput(attrs={'class':'form-control'}),
         }

        labels={
             'TypeStage':'idf Stage',
         }