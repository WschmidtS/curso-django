from django.urls import path

from pypro.demoday.views import video

app_name = 'demoday'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
]
