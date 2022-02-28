from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, devs sem camisa, Você está dentro de polls index')

