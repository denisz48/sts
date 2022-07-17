from django import forms
from django.forms import ModelForm, TextInput
from .models import City 
# Reordering Form and View


class PositionForm(forms.Form):
    position = forms.CharField()
    
    
class CityForm(ModelForm):
    class Meta:
        model = City 
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}