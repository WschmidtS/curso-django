from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render


def home(request):
    #   raise ValueError()
    return render(request, 'base/home.html')
