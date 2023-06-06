from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from import_export.admin import ImportExportMixin

from .models import *


admin.site.index_title = 'Welcome to Admin Dashboard'


class category_list(ImportExportMixin,admin.ModelAdmin):
    list_display = ('id','name','icon',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 15
    exclude = ('id',)

admin.site.register(category,category_list)


class store_list(ImportExportMixin,admin.ModelAdmin):
    list_display = ('storenumber','name','district',)
    list_filter = ('name','storenumber','district',)
    search_fields = ('name','storenumber','district',)
    list_per_page = 15

admin.site.register(store,store_list)

class brand_list(ImportExportMixin,admin.ModelAdmin):
    list_display = ('brand_id','name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 15

admin.site.register(Brand,brand_list)

class District_list(ImportExportMixin,admin.ModelAdmin):
    list_display = ('district_id','name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 15

admin.site.register(District,District_list)




class offerBYcatlist(ImportExportMixin,admin.ModelAdmin):
    list_display = ('category','discount','start_date','end_date','status','District',)
    list_filter = ('category','District',)
    search_fields =('category','discount','start_date','end_date','status',)
    list_per_page = 15
    exclude = ('id',)

admin.site.register(offers_by_category,offerBYcatlist)

class offerBYprodlist(ImportExportMixin,admin.ModelAdmin):
    list_display = ('category','product_name','MRP','discount_rate','start_date','end_date','status',)
    list_filter = ('category','product_name',)
    search_fields =('category','product_name','MRP','discount_rate','start_date','end_date','status',)
    list_per_page = 15

admin.site.register(offers_by_product,offerBYprodlist)


# add below list display

     # def get_urls(self):
    #     urls = super().get_urls()
    #     new_urls = [path('upload-csv/', self.upload_csv),]
    #     return new_urls + urls

    # def upload_csv(self, request):
    #     if request.method == "POST":
    #         csv_file = request.FILES["csv_upload"]
            
    #         if not csv_file.name.endswith('.csv'):
    #             messages.warning(request, 'The wrong file type was uploaded')
    #             return HttpResponseRedirect(request.path_info)
            
    #         file_data = csv_file.read().decode("utf-8")
    #         csv_data = file_data.split("\n")

    #         for x in csv_data:
    #             fields = x.split(",")
    #             created = offers_by_category.objects.update_or_create(
    #                 category = fields[0],
    #                 website_link = fields[1],
    #                 discount = fields[2],
    #                 start_date = fields[3],
    #                 end_date = fields[4],
    #                 status = fields[5],
    #                 )
    #         url = reverse('admin:index')
    #         return HttpResponseRedirect(url)

    #     form = CsvImportForm()
    #     data = {"form": form}
    #     return render(request, "admin/csv_upload.html", data)


    # class CsvImportForm(forms.Form):
#     csv_upload = forms.FileField()