from .forms import (ContactForm)
from django.shortcuts import render, redirect
from django.views import View


class Contact(View):
    def get(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            form.save()
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'contact/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST, request.FILES)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('thankyou')

            else:
                return redirect('contact')


"""
This is response 'Thank you' page view,
when the contact page is sending and turn out
the page to 'Thank you'

"""


class Thank_You(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact/thankyou.html')
