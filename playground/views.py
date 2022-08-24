from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x = 1
    y = 2 
    return x

# Create your views here.

# view function it takes a request and return a response 
#request handler

def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Deo'})
