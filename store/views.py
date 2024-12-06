from django.shortcuts import render
from .models import *
def home(request):
    ctg = Category.objects.all()
    product = Product.objects.all()

    ctx={'ctg':ctg,
         'product':product}
    return render(request,'index.html',ctx)
def product(request, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    product = Product.objects.all().filter(type_id=category.id)

    ctx={'ctg':ctg,
         'category':category,
         'product':product}
    return render(request,'products.html',ctx)