from django.contrib import admin
from .models import RentPlace, District, PaymentMode

admin.site.register(RentPlace)
admin.site.register(District)
admin.site.register(PaymentMode)
