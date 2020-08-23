# Create your views here.
from django.shortcuts import render

from pypro.modulos import facade


def home(request):
    #   raise ValueError()
    return render(request, 'base/home.html', {})
