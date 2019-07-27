from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request,'inquiry/landing.html')

def inquiry(request):
    return render(request,'inquiry/inquiry.html')
