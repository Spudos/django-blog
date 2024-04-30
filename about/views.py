from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

def about(request):
    return HttpResponse("Hello, About!")