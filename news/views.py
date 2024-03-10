from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def news(request):
    return HttpResponse('Привет! Это страница новостей!')


def index(request):
    return HttpResponse('Привет! Это главная страница!')
