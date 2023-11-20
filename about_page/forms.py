from django import forms
from .models import AboutUs
from .widgets import CustomClearableFileInput


class AboutPageForm(forms.ModelForm):

    class Meta:
        model = AboutUs
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)
