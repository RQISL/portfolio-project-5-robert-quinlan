from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from .models import ContactUs, FormDynmaic


# Create your views here.
def contact_us(request):
    """ A view to return the category painting page """
    contactus = ContactUs.objects.all()
    
    context = {
        "contactus": contactus, 
    }

    return render(request, 'contactus/contactus.html', context)

def hireme(request, id):
    """ A view to return the category painting page """
    contactus = FormDynmaic.objects.filter(id=id)
    template = loader.get_template('contactus/hireme.html')
    
    context = {
        "contactus": contactus, 
    }

    return HttpResponse(template.render(context, request))  
