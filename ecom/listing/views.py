from django.shortcuts import render

from .models import Product

# Create your views here.

# products
# get all products
# select * from products;


def product_listing_view(request):
    print("Product listing....")
    products = Product.objects.all()
    print(products)
    return render(request, "listing/shop.html", {
        "products": products
    })


def product_details_view(request, id):
    print("Product Details....", id)
    product = Product.objects.get(id=id)
    context = {
        "product": product, "not_found": False
    }

    return render(request, "listing/product-details.html", context=context)
