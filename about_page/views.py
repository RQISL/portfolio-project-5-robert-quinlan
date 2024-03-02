from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import AboutUs
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AboutPageForm

# Create your views here.


def aboutus(request):
    """ A view to return the about us page """
    about_us = AboutUs.objects.get()

    template = 'aboutus/aboutus.html'

    context = {
        'about_us': about_us,
    }

    return render(request, template, context)


@login_required
def edit_about_page(request):
    """ Edit a home personal page in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('aboutus'))

    about_page = get_object_or_404(AboutUs)
    if request.method == 'POST':
        form = AboutPageForm(request.POST, request.FILES, instance=about_page)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your home',
                             'personal page!')
            return redirect(reverse('aboutus'))
        else:
            messages.error(request, 'Failed to update your personal page.',
                           'Please ensure the form is valid.')
    else:
        form = AboutPageForm(instance=about_page)
        messages.info(request, f'You are editing {about_page.title}')

    template = 'about_us/edit_about_page.html'
    context = {
        'form': form,
        'about_page': about_page,
    }

    return render(request, template, context)
