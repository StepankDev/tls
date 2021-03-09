from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('puestos', views.renting, name='renting'),
    path('socios', views.partners, name='partners'),
    path('blog', views.blog, name='blog'),
    path('post', views.post, name='post'),
    path('contacto', views.contact, name='contact'),
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
]