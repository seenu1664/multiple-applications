from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def one(request):
    return HttpResponse('<h1>I AM VERY GOOD BOY</h1>')
def two(request):
    return HttpResponse('<h1>THIS IS MY LIFE</h1>')