from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def one(request):
    return HttpResponse('<h1> I LIKE NATURE</h1>')
def two(request):
    return HttpResponse('<h1><marquee>THIS IS MY FRIST MAPING</marquee></h1>')
    