from django.shortcuts import render

from .models import ImageSlides

# Create your views here.
def about_us(request):
    """ A view to return the about us page """
    aboutus = ImageSlides.objects.all()
    
    context = {
        "aboutus": aboutus, 
    }

    return render(request, 'aboutus/aboutus.html', context)