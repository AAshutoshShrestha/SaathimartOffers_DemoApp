import django_filters
from .models import offers_by_category,offers_by_product,store

class CategoryWise(django_filters.FilterSet):
	class Meta:
		model = offers_by_category
		fields = ['category','District',]
		exclude = ['discount','status']


class ProductWise(django_filters.FilterSet):
	class Meta:
		model = offers_by_product
		fields =  ['category','brand',]

class Store_wise(django_filters.FilterSet):
	class Meta:
		model = store
		fields =  ['storenumber','district',]

