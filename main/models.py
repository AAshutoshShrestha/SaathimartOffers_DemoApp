from django.db import models

STATUS = (
			('Running', 'Running'),
			('Stopped', 'Stopped'),
			('Upcomming', 'Upcomming'),
			)


class category(models.Model):
    name = models.CharField(max_length=50,null=True)
    icon = models.ImageField(upload_to ='',default='logo.png')

    def __str__(self):
        return self.name

class District(models.Model):
    district_id = models.IntegerField(null=True)
    name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name

class store(models.Model):
    storenumber = models.IntegerField(null=True)
    name = models.CharField(max_length=200,null=True)
    district = models.ForeignKey(District, on_delete= models.SET_NULL, null=True) 

    def __str__(self):
        return self.name

class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True,auto_created = True)
    name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name

class offers_by_category(models.Model):
    category = models.ForeignKey(category, on_delete= models.SET_NULL, null=True) 
    District = models.ForeignKey(District, on_delete= models.SET_NULL, null=True) 
    website_link = models.URLField(max_length=200)
    discount = models.CharField(max_length=200, null=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField( null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)


    def __str__(self):
        return self.discount
    
class offers_by_product(models.Model):
    category = models.ForeignKey(category, on_delete= models.SET_NULL, null=True) 
    product_name = models.CharField(max_length=500, null=True)
    brand = models.ForeignKey(Brand, on_delete= models.SET_NULL, null=True) 
    MRP = models.CharField(max_length=200, null=True)
    discount_rate = models.CharField(max_length=200, null=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField( null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product_name
