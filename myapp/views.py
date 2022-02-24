from tempfile import tempdir
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import randrange

# Create your views here.

def index(request):
    uid = User.objects.get(email=request.session['email'])
    return render(request,'index.html',{'uid':uid})

def login(request):
    try:
        User.objects.get(email=request.session['email'])
        return redirect('index')
    except:
        if request.method == 'POST':
            try:
                uid = User.objects.get(email=request.POST['email'])
                if uid.password == request.POST['password']:
                    request.session['email'] = uid.email
                    return redirect('index')
                return render(request,'login.html',{'msg':'Password is incorrect'})
            except:
                return render(request,'register.html',{'msg':'Email is not registered'})
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        try:
            User.objects.get(email=request.POST['email'])
            return render(request,'register.html',{'msg':'Email is already registered'})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                global temp

                temp = {
                    'name': request.POST['name'],
                    'email' : request.POST['email'],
                    'mobile' : request.POST['mobile'],
                    'address' : request.POST['address'],
                    'password' : request.POST['password'],
                }
                otp = randrange(1000,9999)
                subject = 'welcome to Lab App'
                message = f'Your OTP is {otp}. please enter correctly'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'otp.html',{'otp':otp})

            return render(request,'register.html',{'msg':'Both passwords are not matched'})
    return render(request,'register.html')

def otp(request):
    if request.method == 'POST':
        if request.POST['uotp'] == request.POST['otp']:
            global temp
            User.objects.create(
                name = temp['name'],
                email = temp['email'],
                mobile = temp['mobile'],
                address = temp['address'],
                password = temp['password']
            )
            msg = "Account is Created"
            return render(request,'login.html',{'msg':msg})
        return render(request,'otp.html',{'otp':request.POST['otp'],'msg':'incorrect OTP'})


def logout(request):
    del request.session['email']
    return redirect('login')

def profile(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        uid.name = request.POST['name']
        uid.mobile = request.POST['mobile']
        uid.address = request.POST['address']
        if 'pic' in request.FILES:
            uid.pic = request.FILES['pic']
        uid.save()
        return render(request,'profile.html',{'uid':uid,'msg':'Profile Updated'})
    return render(request,'profile.html',{'uid':uid})

def icons(request):
    return render(request,'icons.html')

def change_password(request):
    uid = User.objects.get(email=request.session['email'])
    if uid.password == request.POST['opassword']:
        if request.POST['npassword'] == request.POST['cpassword']:
            uid.password = request.POST['npassword']
            uid.save()
            return JsonResponse({'msg':'Password Updated'})
        return JsonResponse({'msg':'Both new are not same'})
    return JsonResponse({'msg':'Old Password is wrong'})