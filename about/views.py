from django.shortcuts import render
from .models import AboutUs, BioDetail

# Create your views here.
def aboutus(request):
    """ A view to return the about us page """
    about_us = AboutUs.objects.all()
    about = BioDetail.objects.get()
    
    
    return render(request, 'about/about.html', {'about_us': about_us, 'about': about})

