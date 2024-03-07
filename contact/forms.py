from django import forms
from .models import ContactView

# Create your forms here.


class ContactForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ContactView
        fields = '__all__'
