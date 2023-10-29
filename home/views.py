from django.shortcuts import render
from .models import HomePage, ElenaInfo

def index(request):
    """ A view to return the index page """
    home_page = HomePage.objects.get()
    elena_info = ElenaInfo.objects.get()
    
    return render(request, 'home/index.html', {'home_page': home_page, 'elena_info': elena_info})