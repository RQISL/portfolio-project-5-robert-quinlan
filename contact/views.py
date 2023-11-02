from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail, BadHeaderError

from .forms import ContactForm 
from .models import ContactUs, FormDynmaic


# Create your views here.
def contact_us(request):
    """ A view to return the category painting page """
    contactus = ContactUs.objects.all()
    
    context = {
        "contactus": contactus, 
    }

    return render(request, 'contact/contact.html', context)

def hireme(request, id):
    """ A view to return the category painting page """
    contactus = FormDynmaic.objects.filter(id=id)
    template = loader.get_template('contact/hireme.html')
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
            message = "\n".join(body.values())
            
            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("contact/contact.html")
            
    form = ContactForm()
    context = {
        "contactus": contactus,
        "form": form 
    }

    return HttpResponse(template.render(context, request))  
    