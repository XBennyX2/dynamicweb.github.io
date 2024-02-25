from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.
def home(requests):
    info = CompanyInformation.objects.all().first()
    products = Product.objects.all()

    data = {
        'info':info,
        'products':products,

    }

    return render(requests, 'home.html', data)

def about(requests):
    about = About.objects.all().first()
    contacts = Contact.objects.all().first()

    data = {
        'A':about,
        'Con':contacts

    }
    return render(requests, 'about.html', data)




def contacts(requests):
    contacts = Contact.objects.all().first()
    data = {
        'Con':contacts
    }
    return render(requests, 'contact.html', data)