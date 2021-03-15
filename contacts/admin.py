from django.contrib import admin
from .models import Contact, ContactRent, ContactPartner

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'last_name', 'email')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactRent, ContactAdmin)
admin.site.register(ContactPartner, ContactAdmin)
