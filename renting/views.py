from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from .choices import district_choices, payment_choices
from . models import *

def index(request):
    rents = RentPlace.objects.order_by('-date_published').filter(is_published=True)
    paginator = Paginator(rents, 3)
    page = request.GET.get('page')
    paged_rents = paginator.get_page(page)

    district_choices = District.objects.all()
    payment_choice = PaymentMode.objects.all()

    context = {
        'rents': paged_rents,
        'district_choices': district_choices,
        'payment_choices': payment_choices
    }
    
    return render(request, 'pages/renting.html', context)

def rent(request, rent_id):
    rent = get_object_or_404(RentPlace, pk=rent_id)
    context = {
        'rent': rent
    }
    return render(request, 'pages/renting_place.html', context)
