from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse

def index_view(request):
    return HttpResponse('<h2>Home Page</h2>')

def about_view(request):
    return HttpResponse('<h2>About Page</h2>')

def contact_view(request):
    return HttpResponse('<h2>Contact Page</h2>')