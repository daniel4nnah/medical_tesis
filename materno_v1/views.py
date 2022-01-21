from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'materno_v1/dashboard.html')

def profile(request):
    return render(request, 'materno_v1/profile.html')