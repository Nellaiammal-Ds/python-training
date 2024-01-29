from django.shortcuts import render
from django.http import HttpResponse

def displaymsg(request):
    return HttpResponse("Haii,this is my msg")

# Create your views here.
