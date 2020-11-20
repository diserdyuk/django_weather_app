from django.http import HttpResponse 


def index(req):
    return HttpResponse('<h1>Weather is good!</h1>')




