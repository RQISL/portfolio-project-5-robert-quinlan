from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.template import loader
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, CategoryContactForm
from .models import ContactUs


# Create your views here.
def contact_us(request):
    """A view to return the category painting page"""
    contactus = ContactUs.objects.all()

    context = {
        "contactus": contactus,
    }

    return render(request, "contact/contact.html", context)


def hireme(request, id):
    """A view to return the category painting page"""
    contactus = ContactUs.objects.get(id=id)
    template = loader.get_template("contact/hireme.html")

    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email_address"],
                "message": form.cleaned_data["message"],
                "image": form.cleaned_data["image"],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, "admin@example.com",
                          ["admin@example.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("contact/contact.html")

    form = ContactForm()
    context = {"contactus": contactus, "form": form}

    return HttpResponse(template.render(context, request))


# CRUD managements for category in Category Painting page


@login_required
def add_contact_category(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("contact"))

    if request.method == "POST":
        form = CategoryContactForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("contact"))
        else:
            messages.error(
                request, "Failed to add product. Please ensure",
                         "the form is valid."
            )
    else:
        form = CategoryContactForm()

    template = "contact/add_contact_category.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_contact_category(request, contact_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("contact"))

    contact_category = get_object_or_404(ContactUs, pk=contact_id)
    if request.method == "POST":
        form = CategoryContactForm(
            request.POST, request.FILES, instance=contact_category
        )
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated contact category!")
            return redirect(reverse("edit_category",
                            args=[contact_category.id]))
        else:
            messages.error(
                request,
                "Failed to update cotact category. Please ensure the form",
                "is valid."
            )
    else:
        form = CategoryContactForm(instance=contact_category)
        messages.info(request, f"You are editing {contact_category.name}")

    template = "contact/edit_contact_category.html"
    context = {
        "form": form,
        "contact_category": contact_category,
    }
    print(contact_category)
    return render(request, template, context)


@login_required
def delete_contact_category(request, contact_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("contact"))

    category = get_object_or_404(ContactUs, pk=contact_id)
    category.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("contact"))
