from django.shortcuts import render

from .models import ContactUs

# Create your views here.
def contact_us(request):
    """ A view to return the category painting page """
    contactus = ContactUs.objects.all()
    
    context = {
        "contactus": contactus, 
    }

    return render(request, 'contactus/contactus.html', context)