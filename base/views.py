from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, welcome to StudyBud!")

def room(request):
    return HttpResponse("This is a room page")