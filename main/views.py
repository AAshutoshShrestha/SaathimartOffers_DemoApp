from django.db.models import query
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import *
from .filters import *


def bycategory(request):
    query_list = offers_by_category.objects.all()
    categoryFilter = CategoryWise(request.GET, queryset=query_list)
    offers = categoryFilter.qs 
    context = {
        'Offer' : offers,
        'filter': categoryFilter
    }
    return render(request, 'views/by_category.html',context)

def byproduct(request):
    query_list = offers_by_product.objects.all()
    categoryFilter = ProductWise(request.GET, queryset=query_list)
    offers = categoryFilter.qs  
    context = {
        'offers' : offers,
        'filter': categoryFilter
    }
    return render(request, 'views/by_product.html',context)

def stores(request):
    query_list = store.objects.all()
    storeFilter = Store_wise(request.GET, queryset=query_list)
    offers = storeFilter.qs  
    context = {
        'offers' : offers,
        'filter': storeFilter
    }
    return render(request, 'views/storedetails.html',context)