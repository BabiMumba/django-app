from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello Django</h1>")

def about(request):
    return HttpResponse("<h1>Apropos de la page developpement</h1>")


