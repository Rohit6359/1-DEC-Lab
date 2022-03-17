from django.db import models
from myapp.models import *
# Create your models here.

class ClientUser(models.Model):

    choices = (('male','male'),('female','female'),('other','other'))

    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    password = models.CharField(max_length=25)
    address = models.TextField()
    aadhar = models.CharField(max_length=12)
    gender = models.CharField(max_length=20,choices=choices)
    age = models.IntegerField()

    def __str__(self):
        return self.fname + '   ' +  self.lname

class Inquiry(models.Model):

    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    des = models.TextField()
    inq_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

class BookingTest(models.Model):
    
    choices = (('Online','Online'),('On Clinic','On Clinic'))
    time_choice = (('Morning','Morning'),('Afternoon','Afternoon'),('Evening','Evening'))

    client = models.ForeignKey(ClientUser,on_delete=models.CASCADE)
    test = models.ForeignKey(Test,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.CharField(max_length=50,choices=time_choice,default='Morning')
    book_time = models.DateTimeField(auto_now_add=True)
    pay_type = models.CharField(max_length=50,choices=choices)
    pay_verify = models.BooleanField(default=False)
    pay_id = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.test.title 


