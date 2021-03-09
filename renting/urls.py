from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='renting'),
    path('<int:rent_id>', views.rent, name='rent'),
]