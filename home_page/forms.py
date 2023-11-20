from django import forms
from .models import HomePage, ExhibationView
from .widgets import CustomClearableFileInput


class HomePageForm(forms.ModelForm):

    class Meta:
        model = HomePage
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)


class ExhibationViewForm(forms.ModelForm):

    class Meta:
        model = ExhibationView
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)
