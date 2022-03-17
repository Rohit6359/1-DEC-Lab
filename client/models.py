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

    client = models.ForeignKey(ClientUser,on_delete=models.CASCADE)
    test = models.ForeignKey(Test,on_delete=models.CASCADE)
    date = models.DateField()
    book_time = models.DateTimeField(auto_now_add=True)
    pay_type = models.CharField(max_length=50,choices=choices)

    def __str__(self):
        return self.test.title 


