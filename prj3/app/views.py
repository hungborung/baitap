from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic.detail import DetailView
from cart.cart import Cart

# Create your views here.

priceList = [
    {'id': 1, 'name': '0đ - 150,000đ', 'max': 150000},
    {'id': 2, 'name': '150,000đ-500,000đ', 'min': 151000, 'max': 500000},
    {'id': 3, 'name': 'Trên 500,000đ', 'min': 501000},
]

def index(request):
    product = Product.objects.filter(is_featured=True)

    listCategory = Category.objects.filter(cat_parent=None)
    cart = Cart(request)

    context = {
        'product' : product,
        'listCategory' : listCategory,
        'cart': cart,
      
    }
    return render(request, 'index.html', context)

def categorydetail(request, slug):
    name = request.GET.get('name', '')
    publisherId = request.GET.get('publisherId')
    publisher = Publisher.objects.all()
    category = get_object_or_404(Category, slug=slug)
    product = Product.objects.filter(category=category.id)
    productList = product.filter(name__icontains=name)
    publisherId = int(publisherId) if publisherId else None

    if publisherId:
        productList = productList.filter(publisher__id=publisherId)

    priceId = request.GET.get('priceId')
    priceId = int(priceId) if priceId else None
    price = priceList[priceId-1] if priceId else {}
    minPrice, maxPrice = price.get('min'), price.get('max')
    if minPrice:
        productList = productList.filter(price_sell__gte=minPrice)
    if maxPrice:
        productList = productList.filter(price_sell__lte=maxPrice)


    

    context = {
        'category': category,
        'product': product,
        'publisher' : publisher,
        'name': name,
        'productList': productList,
        'publisherId': publisherId,
        'priceId': priceId,
        'priceList': priceList,
        
    }
    return render(request, 'category.html', context)


def productdetail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    cart = Cart(request)

    if product.discount > 0:
        price_discount = product.price_sell * ((100-product.discount)/100)
    else:
        price_discount = product.price_sell
        
    context = {
        'product': product,
        'cart': cart,
        'price_discount': price_discount,
    }

    return render(request, 'productdetail.html', context)


