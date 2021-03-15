from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('puestos', views.renting, name='renting'),
    path('contacto', views.contact, name='contact'),

    path('socios', views.partners, name='partners'),
    path('planes-socios', views.partnerPricing, name='partnerPricing'),
    path('blog', views.blog, name='blog'),
    path('post', views.post, name='post'),
    path('registro-basico', views.registerBasic, name='registerBasic'),
    path('registro', views.register, name='register'),
    path('login', views.login, name='login'),
    path('cuenta', views.account, name='account'),
    path('planes', views.rentingpricing, name='rentingpricing'),
    
    path('lugar', views.rentingplace, name='rentingplace'),

    path('socio', views.partner, name='partner'),

    path('basico', views.basicCheckOut, name='basicCheckOut'),
    path('sersocio', views.partnerPublish, name='partnerPublish'),
    path('loginbasico', views.loginBasic, name='loginBasic'),
    path('intermedio', views.intermediateCheckOut, name='intermediateCheckOut'),
    path('avanzado', views.advancedCheckOut, name='advancedCheckOut'),
    path('pago', views.payment, name='payment'),
    path('pago-socio', views.payment_partner, name='payment_partner'),
]