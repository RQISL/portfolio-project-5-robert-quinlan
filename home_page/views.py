from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import HomePage, ExhibationView
from .forms import HomePageForm, ExhibationViewForm


def index(request):
    """ A view to return the index page """
    home_personal = HomePage.objects.get()
    template = 'home/index.html'

    context = {
        'home_personal': home_personal
    }

    return render(request, template, context)


def exhibation(request):
    """ A view to return the index page """
    exhibations = ExhibationView.objects.all()
    template = 'home/exhibations.html'

    context = {
        'exhibations': exhibations
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
            messages.success(request, 'Successfully updated your home'
                                      'personal page!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to update your personal page.',
                                    'Please ensure the form is valid.')
    else:
        form = HomePageForm(instance=home)
        messages.info(request, f'You are editing {home.head}')

    template = 'home/edit_home_page.html'
    context = {
        'form': form,
        'home': home,
    }

    return render(request, template, context)


@login_required
def add_exhibation(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('exhibations'))

    if request.method == 'POST':
        form = ExhibationViewForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            messages.success(request, 'Successfully added exhibation!')
            return redirect(reverse('exhibations'))
        else:
            messages.error(request, 'Failed to add exhibation. Please ensure',
                                    'the form is valid.')
    else:
        form = ExhibationViewForm()

    template = 'home/add_exhibations.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_exhibation(request):
    """ Edit a hoe personal page in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('edit_exhibations'))

    exhibation_view = get_object_or_404(ExhibationView)
    if request.method == 'POST':
        form = ExhibationView(request.POST, request.FILES,
                              instance=exhibation_view)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated your exhibation',
                                      'page!')
            return redirect(reverse('edit_exhibations'))
        else:
            messages.error(request, 'Failed to update your exhibations page.',
                                    'Please ensure the form is valid.')
    else:
        form = ExhibationView(instance=exhibation_view)
        messages.info(request, f'You are editing {exhibation.name}')

    template = 'home/edit_exhibations.html'
    context = {
        'form': form,
        'exhibation_view': exhibation_view,
    }

    return render(request, template, context)
