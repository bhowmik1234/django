from django.http import HttpResponse
from django.shortcuts import render

def home(request):
#    return HttpResponse("hello world, at home") 
    return render(request, 'layout.html')

# def about(request):
#    return HttpResponse("hello world, at about") 

def about(request):
   return render(request, 'website/index.html')
