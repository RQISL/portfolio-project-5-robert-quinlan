from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import HomePage
from .forms import HomePageForm

def index(request):
    """ A view to return the index page """
    home_personal = HomePage.objects.get()
    template = 'home/index.html'

    context = {
        'home_personal': home_personal
    }

    return render(request, template, context)

@login_required
def edit_home_page(request):
    """ Edit a hoe personal page in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    home = get_object_or_404(HomePage)
    if request.method == 'POST':
        form = HomePageForm(request.POST, request.FILES, instance=home)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your home personal page!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to update your personal page. Please ensure the form is valid.')
    else:
        form = HomePageForm(instance=home)
        messages.info(request, f'You are editing {home.head}')

    template = 'home/edit_home_page.html'
    context = {
        'form': form,
        'home': home,
    }

    return render(request, template, context)