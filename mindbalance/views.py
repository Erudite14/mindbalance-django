from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'servers.html')


def about(request):
    return HttpResponse('about')