from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost
from renting.models import RentPlace
from .forms import SignUpForm
from .forms import partnerForm
from .forms import SignUpFormBasic
from .forms import basicRent
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import login as user_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    posts = BlogPost.objects.order_by('-date_published').filter(is_published=True)
    rents = RentPlace.objects.order_by('-date_published').filter(is_published=True)

    context = {
        'posts': posts,
        'rents': rents
    }
    return render(request, 'pages/index.html', context)

def renting(request):
    return render(request, 'pages/renting.html')

def partners(request):
    return render(request, 'pages/partners.html')

def blog(request):
    return render(request, 'pages/blog.html')

def post(request):
    return render(request, 'pages/post.html')

def contact(request):
    return render(request, 'pages/contact.html')

# MAIN LOGIN FROM FRONT PAGE
def login(request):
    _message = 'Please sign in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                user_login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message}
    return render(request, 'pages/login.html', context)

# SECONDARY REGISTER FROM RENT A PLACE
def registerBasic(request):
    if request.method == 'POST':
        form = SignUpFormBasic(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user_login(request, user)
            return redirect('basicCheckOut')
    else:
        form = SignUpFormBasic()
    return render(request, 'pages/payment-register.html', {'form': form})

# MAIN REGISTER FROM HOME PAGE 
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'pages/success.html', {'form': form})

@login_required(login_url='login')
def account(request):
    return render(request, 'pages/login.html')

def loginBasic(request):
    return render(request, 'pages/login_basic.html')

def rentingpricing(request):
    return render(request, 'pages/renting_pricing.html')

def rentingplace(request):
    return render(request, 'pages/renting_place.html')

def partner(request):
    return render(request, 'pages/partner.html')

@login_required(login_url='loginBasic')
def basicCheckOut(request):
    
    template_name = 'pages/basic.html'
    
    object = None
    if request.method == 'POST':
        form = basicRent(request.POST, request.FILES)
        if form.is_valid():
            object = form.save()
            return redirect('payment')
            if not request.is_ajax():
                # reload the page
                next = request.META['PATH_INFO']
                return HttpResponseRedirect(next)
            # if is_ajax(), we just return the validated form, so the modal will close
    else:
        form = basicRent()
    
    return render(request, template_name, {
        'form': form,
        'object': object,
        })


def intermediateCheckOut(request):
    return render(request, 'pages/intermediate.html')

def advancedCheckOut(request):
    return render(request, 'pages/advanced.html')

def payment(request):
    return render(request, 'pages/payment.html')

def partnerPublish(request):
    
    template_name = 'pages/partner-publish.html'
    
    object = None
    if request.method == 'POST':
        form = partnerForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save()
            return redirect('payment')
            if not request.is_ajax():
                # reload the page
                next = request.META['PATH_INFO']
                return HttpResponseRedirect(next)
            # if is_ajax(), we just return the validated form, so the modal will close
    else:
        form = partnerForm()
    
    return render(request, template_name, {
        'form': form,
        'object': object,
        })


