from django.urls import path

from store.views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('product/<slug>', product, name = 'product')
]