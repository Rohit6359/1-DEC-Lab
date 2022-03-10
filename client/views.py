from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'clientindex.html')
def about(request):
    return render(request,'about.html')
def codes(request):
    return render(request,'codes.html')
def contact(request):
    return render(request,'contact.html')
def header(request):
    return render(request,'header.html')
def treatments(request):
    return render(request,'treatments.html')