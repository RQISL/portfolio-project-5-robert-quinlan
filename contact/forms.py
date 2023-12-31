from django import forms
from .widgets import CustomClearableFileInput
from .models import ContactUs

# Create your forms here.


class ContactForm(forms.Form):
    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )
    first_name = forms.CharField(
        label="First Name", widget=forms.TextInput(attrs={"placeholder": "First name"})
    )
    last_name = forms.CharField(
        label="Last Name", widget=forms.TextInput(attrs={"placeholder": "Last name"})
    )
    email_address = forms.EmailField(
        label="Email address",
        widget=forms.TextInput(attrs={"placeholder": "Email Address"}),
    )
    message = forms.CharField(
        max_length=2000,
        label="Message",
        widget=forms.Textarea(attrs={"placeholder": "Write to your message"}),
    )


class CategoryContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )
