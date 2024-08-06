from django.shortcuts import render
from mainapp.models import Product
from django.db.models import Q

# Create your views here.
def search(req):
    products = None
    query = None
    if 'q' in req.GET:
        query = req.GET.get('q')
        print(query)
        products = Product.objects.filter(Q(name__icontains=query) | Q(detail__icontains=query))
    return render(req, 'search.html', {'query': query, 'products': products})
