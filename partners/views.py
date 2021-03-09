from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from . models import *

def index(request):
    partners = PartnerInfo.objects.order_by('-date_published').filter(is_published=True)
    paginator = Paginator(partners, 6)
    page = request.GET.get('page')
    paged_partners = paginator.get_page(page)

    context = {
        'partners': paged_partners
    }
    return render(request, 'pages/partners.html', context)

def partner(request, partner_id):
    partner = get_object_or_404(PartnerInfo, pk=partner_id)
    context = {
        'partner': partner
    }
    return render(request, 'pages/partner.html', context) 
