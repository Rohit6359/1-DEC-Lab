from django.db import models

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