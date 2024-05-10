from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.core.mail import send_mail

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import JsonResponse
import json

def homepage(request):
    # logout(request)
    context = {'page': {}}
    return render(request, 'Churn/index.html', context)

def logout_view(request):
    logout(request) 
    return redirect('home')

def telecompage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {'page': {}}
    return render(request, 'Churn/Telecom.html', context)


def customerpage(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {'page': {}}
    return render(request, 'Churn/Customer.html', context)

def aboutpage(request):
    context = {'page': {}}
    return render(request, 'Churn/AboutUs.html', context)

def loginpage(request):
    context = {'page': {}}
    return render(request, 'Churn/Sign.html', context)

def savepage(request):
    if request.method == 'POST' and not request.POST.get("username"):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.get(email=email)

        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    elif request.method == 'POST' and request.POST.get("username"):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username,email,password)

        user.save()
        
    return render(request, 'Churn/Sign.html')

def contactpage(request):
    context = {'page': {}}
    return render(request, 'Churn/Contact.html', context)

def send_email(request):
    # CONTACT FORM
    try:
        if request.method == 'POST':
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            form_data = {
                'firstname':firstname,
                'lastname':lastname,
                'email':email,
                'phone':phone,
                'message':message,
            }
            message = '''Email:\t{}\n From:\t{} {}\n Message:\t{}\n Phone:\t{}'''.format(form_data['email'], form_data['firstname'], form_data['lastname'], form_data['message'], form_data['phone'])
            send_mail('Email from ChurnShield!', message, '', ['helpdesk.churnsheild@gmail.com']) #
            
    finally:
        context = {'page': {}}
        return render(request, 'Churn/Contact.html', context)

def custompage(request):
    context = {'page': {}}
    return render(request, 'Churn/Custom.html', context)

def faqpage(request):
    context = {'page': {}}
    return render(request, 'Churn/FAQs.html', context)
