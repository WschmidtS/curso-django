from django.urls import path

from pypro.demoday.views import video, indice

app_name = 'demoday'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('', indice, name='indice'),
]
