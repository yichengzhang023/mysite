from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def other(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    return render(request, 'index.html')
