from django.http import HttpResponse
from django.shortcuts import redirect, render
from myapp.models import *
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import randrange


# Create your views here.

def index(request):
    tests = Test.objects.filter(verify=True,test_on=True)
    try:
        uid = ClientUser.objects.get(email=request.session['username'])
        return render(request,'clientindex.html',{'tests':tests,'uid':uid})
    except:
        return render(request,'clientindex.html',{'tests':tests})

def client_logout(request):
    del request.session['username']
    return redirect('cindex')

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
    try:
        ClientUser.objects.get(email=request.session['username'])
        return redirect('cindex')
    except:
        if request.method == 'POST':
            try:
                uid = ClientUser.objects.get(email=request.POST['email'])
                if uid.password == request.POST['password']:
                    request.session['username'] = uid.email
                    return redirect('cindex')
                return render(request,'signin.html',{'msg':'Password is incorrect'})
            except:
                return render(request,'signup.html',{'msg':'Email is not registered'})
        return render(request,'signin.html')

def book_test(request,pk):
    try:
        uid = ClientUser.objects.get(email=request.session['username'])
        test = Test.objects.get(id=pk)
        return render(request,'book-appoinment.html',{'uid':uid,'test':test})
    except:
        return redirect('signin')

def view_test(request,pk):
    test = Test.objects.get(id=pk)
    return render(request,'view-test.html',{'test':test})


def signup(request):
    if request.method == 'POST':
        try:
            ClientUser.objects.get(email=request.POST['username'])
            return render(request,'signup.html',{'msg':'Email is already registered'})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                global temp

                temp = {
                    'fname': request.POST['first_name'],
                    'lname': request.POST['last_name'],
                    'email' : request.POST['email'],
                    'mobile' : request.POST['phone'],
                    'password' : request.POST['password'],
                    'address' : request.POST['address'],
                    'aadhar' : request.POST['aadhar'],
                    'gender' : request.POST['gender'],
                    'age' : request.POST['birthday']
                }
                otp = randrange(1000,9999)
                subject = 'welcome to Lab App'
                message = f'Your OTP is {otp}. please enter correctly'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail( subject, message, email_from, recipient_list )
                return render(request,'cotp.html',{'otp':otp})
            return render(request,'signup.html',{'msg':'Both passwords are not matched'})
    return render(request,'signup.html')


def cotp(request):
    if request.method == 'POST':
        if request.POST['uotp'] == request.POST['otp']:
            global temp
            ClientUser.objects.create(
                fname = temp['fname'],
                lname = temp['lname'],
                email = temp['email'],
                mobile = temp['mobile'],
                password = temp['password'],
                address = temp['address'],
                aadhar = temp['aadhar'],
                gender = temp['gender'],
                age = temp['age']
            )
            msg = "Account is Created"
            return render(request,'signin.html',{'msg':msg})
        return render(request,'cotp.html',{'otp':request.POST['otp'],'msg':'incorrect OTP'})
    return render(request,'cotp.html')


def proceed_test(request,pk):
    uid = ClientUser.objects.get(email=request.session['username'])
    test = Test.objects.get(id=pk)
    if request.method == 'POST':
        if request.POST['pay'] == 'On Clinic':
            book = BookingTest.objects.create(
                client = uid,
                test = test,
                date = request.POST['date'],
                time =  request.POST['time'],
                pay_type = request.POST['pay']
            )
            return render(request,'bookconfirm.html',{'uid':uid,'book':book})
        return HttpResponse('Online Payment Coming Soon!!')
    return redirect('signin')
