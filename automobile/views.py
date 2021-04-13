from django.shortcuts import render
from .models import Car

# Create your views here.

def home(request):
    cars = Car.objects.all()
    return render(request, 'pages/index.html', {'cars': cars})


def about(request):
    return render(request, 'pages/about.html')


def search(request):
    return render(request, 'pages/search.html')


def contact(request):
    return render(request, 'pages/contact.html')


def cars(request):
    cars = Car.objects.all()
    return render(request, 'cars/cars.html', {'cars': cars})


def car_detail(request, id):
    car = Car.objects.get(id=id)
    return render(request, 'cars/car_detail.html', {'car': car})