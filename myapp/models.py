from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=25)
    pic = models.FileField(upload_to='Profile Pic',default='avtar.png')

    def __str__(self):
        return self.email

class Test(models.Model):

    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    des = models.TextField()
    price = models.IntegerField()
    verify = models.BooleanField(default=False)
    approve_by = models.CharField(max_length=100,null=True,blank=True)
    reject = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    test_on = models.BooleanField(default=False)

    def __str__(self):
        return self.title
