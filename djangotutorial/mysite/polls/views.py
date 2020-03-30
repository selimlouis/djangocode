from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(redquest):
    return HttpResponse("Hello, world. Youre at the index.")