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

    path('blog', views.blog, name='blog'),
    path('post', views.post, name='post'),
    path('registro-basico', views.registerBasic, name='registerBasic'),
    path('registro', views.register, name='register'),
    path('login', views.login, name='login'),
    path('cuenta', views.account, name='account'),
    path('planes', views.rentingpricing, name='rentingpricing'),
    
    path('lugar', views.rentingplace, name='rentingplace'),

    path('basico', views.basicCheckOut, name='basicCheckOut'),
    path('loginbasico', views.loginBasic, name='loginBasic'),
    path('intermedio', views.intermediateCheckOut, name='intermediateCheckOut'),
    path('avanzado', views.advancedCheckOut, name='advancedCheckOut'),
    path('pago', views.payment, name='payment'),
]