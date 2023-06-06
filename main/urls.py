from django.urls import path

from . import views

urlpatterns = [
    path('', views.bycategory, name='bycategory'),
    path('products', views.byproduct, name='byproduct'),
    path('stores', views.stores, name='stores'),
]