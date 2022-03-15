from django.http import HttpResponse
from django.shortcuts import redirect, render
from myapp.models import *
from .models import *

# Create your views here.

def index(request):
    tests = Test.objects.filter(verify=True,test_on=True)
    return render(request,'clientindex.html',{'tests':tests})

def about(request):
    admins = User.objects.all()
    return render(request,'about.html',{'admins':admins})

def codes(request):
    return render(request,'codes.html')

def contact(request):
    return render(request,'contact.html')

def header(request):
    return render(request,'header.html')

def treatments(request):
    return render(request,'treatments.html')

def inquiry(request):
    Inquiry.objects.create(
        fullname = request.POST['name'],
        mobile = request.POST['mobile'],
        email = request.POST['email'],
        des = request.POST['des']
    )
    return redirect('cindex')

def signin(request):
    return render(request,'signin.html')
  

def book_test(request,pk):
    try:
        client = ClientUser.objects.get(email=request.session['username'])
        
    except:
        return redirect('signin')

def view_test(request,pk):
    test = Test.objects.get(id=pk)
    return render(request,'view-test.html',{'test':test})