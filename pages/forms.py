from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from datetime import datetime

from renting.models import * 

from renting.models import RentPlace
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre' }), label = '')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido' }), label = '')
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email' }), label = '')
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario' }), label = '')
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña' }), label = '')
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirme su contraseña' }), label = '')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class SignUpFormBasic(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre' }), label = '')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido' }), label = '')
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email' }), label = '')
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario' }), label = '')
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña' }), label = '')
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirme su contraseña' }), label = '')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class basicRent(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título' }), label = '')
    date_published = forms.DateField(widget=forms.HiddenInput(), required=False, label = '')
    price = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Precio en soles' }), label = '')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre' }), label = '')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido' }), label = '')
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono' }), label = '')
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección del puestito' }), label = '')
    district = forms.ModelChoiceField(queryset=District.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control' }), label = '')
    reference = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Referencias del lugar' }), label = '')
    payment = forms.ModelChoiceField(queryset=PaymentMode.objects.all(), empty_label=None, widget=forms.Select(attrs={'class': 'form-control' }), label = '')
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del puestito' }), required=False)
    #main_image = forms.ImageField(upload_to='photos/%Y/%m/%d/', null=True, blank=True, required=False)
    
    is_published = forms.BooleanField(label='', widget=forms.HiddenInput(), required=False, initial=False)
    class Meta:
        model = RentPlace
        fields = ('title', 'price', 'first_name', 'last_name', 'phone', 'address', 'district', 'reference', 'payment', 'description', 'main_image')
