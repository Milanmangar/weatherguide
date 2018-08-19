from django.forms import ModelForm, TextInput
from .models import City,CityUser

class CityForm(ModelForm):
    class Meta:
        model = CityUser
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input form-control', 'placeholder' : 'City Name'})}
