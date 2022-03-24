from django.http import HttpResponse
from django.shortcuts import redirect, render
from myapp.models import *
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import randrange
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest


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

def client_profile(request):
    uid = ClientUser.objects.get(email=request.session['username'])
    if request.method == 'POST':
        uid.fname = request.POST['fname']
        uid.lname = request.POST['lname']
        uid.gender = request.POST['gender']
        uid.age = request.POST['age']
        uid.mobile = request.POST['mobile']
        uid.aadhar = request.POST['aadhar']
        uid.address = request.POST['address']
        uid.save()
        return render(request,'client-profile.html',{'uid':uid,'msg':'Profile Updated'})
    return render(request,'client-profile.html',{'uid':uid})

def change_password(request):
    try:
        uid = ClientUser.objects.get(email=request.session['username'])
        if uid.password==request.POST['opassword']:
            if request.POST['npassword']==request.POST['cpassword']:
                uid.password=request.POST['npassword']
                uid.save()
                return render(request,'change-password.html',{'msg':'Password Updated'})
            return render(request,'change-password.html',{'msg':'Both new Password are not same'})
        return render(request,'change-password.html',{'uid':uid,'msg':'Old Password is wrong'})
    except:
        return render(request,'change-password.html',{'uid':uid})
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

def invoice(request,pk):
    book = BookingTest.objects.get(id=pk)
    return render(request,'invoice.html',{'book':book})

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
        else:
            book = BookingTest.objects.create(
                client = uid,
                test = test,
                date = request.POST['date'],
                time =  request.POST['time'],
                pay_type = request.POST['pay']
            )
            currency = 'INR'
            amount = int(book.test.price)*100  # Rs. 200
        
            # Create a Razorpay Order
            razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                            currency=currency,
                                                            payment_capture='0'))
        
            # order id of newly created order.
            razorpay_order_id = razorpay_order['id']
            callback_url = f'paymenthandler/{book.id}'
        
            # we need to pass these details to frontend.
            context = {}
            context['razorpay_order_id'] = razorpay_order_id
            context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
            context['razorpay_amount'] = amount
            context['currency'] = currency
            context['callback_url'] = callback_url
            context['uid'] = uid
            context['book'] = book
            return render(request,'bookconfirm.html',context=context)

    return redirect('signin')


 
# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request,pk):
    uid = ClientUser.objects.get(email=request.session['username'])
    book = BookingTest.objects.get(id=pk)
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            # if result is None:
            amount = int(book.test.price)*100  # Rs. 200
            try:

                # capture the payemt
                razorpay_client.payment.capture(payment_id, amount)
                book.pay_verify = True
                book.pay_id = payment_id
                book.save()
                # render success page on successful caputre of payment
                return render(request, 'success.html')
            except:

                # if there is an error while capturing payment.
                return render(request, 'fail.html')
            # else:

            #     # if signature verification fails.
            #     return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()