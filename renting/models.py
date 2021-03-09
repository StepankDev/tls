from django.db import models
from datetime import datetime

class District(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class PaymentMode(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class RentPlace(models.Model):
    title = models.CharField(max_length=200)
    date_published = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    phone = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200)
    district = models.ForeignKey(District, null=True, blank=True, on_delete=models.CASCADE)
    reference = models.CharField(max_length=200)
    payment = models.ForeignKey(PaymentMode, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField()
    main_image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
