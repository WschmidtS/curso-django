from django.http import HttpResponse


# Create your views here.


def home(request):
    #   raise ValueError()
    return HttpResponse('<html><body>Olá Django by WschmidtS</body></html>')
