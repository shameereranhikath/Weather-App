from django.forms import ModelForm, TextInput
from .models import City


class CityCreateForm(ModelForm):
    model = City
    fields = ['name']
    widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'Enter Name'})}
