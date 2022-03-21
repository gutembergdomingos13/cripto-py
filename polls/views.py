from urllib import response
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, sem camisa, Você está dentro de polls index')

def detail(request, question_id):
    response = 'Você está buscando a pesgunta %s.'
    return HttpResponse(response % question_id)

def results(request, question_id):
    response = 'Você está olhando o resultado da pergunta %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response = 'Você está votando na pergunta %s.'
    return HttpResponse(response % question_id)

