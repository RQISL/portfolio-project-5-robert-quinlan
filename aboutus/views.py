from django.shortcuts import render

from .models import AboutPersonal

# Create your views here.
def aboutus(request):
    """ A view to return the about us page """
    about_us = AboutPersonal.objects.all()
    
    context = {
        "about_us": about_us, 
    }

    return render(request, 'aboutus/aboutus.html', context)