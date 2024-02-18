from django.shortcuts import render


def search_product(request):
    """ A view to return the index page """

    return render(request, 'search_product/search_product.html')
