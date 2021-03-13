from django.db import models
from datetime import datetime
from renting.models import *

class PartnerInfo(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    document = models.CharField(max_length=200)
    email = models.EmailField()
    date_published = models.DateTimeField(default=datetime.now, blank=True)
    ruc = models.CharField(max_length=9)

    business_name = models.CharField(max_length=200)
    business_address = models.CharField(max_length=200)
    business_type = models.CharField(max_length=200)
    business_products = models.CharField(max_length=200)
    business_references = models.CharField(max_length=200)
    business_description = models.TextField()
    business_district = models.ForeignKey(District, null=True, blank=True, on_delete=models.CASCADE)

    profile_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
