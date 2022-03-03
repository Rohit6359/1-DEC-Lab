from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile']

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['title','id','price','verify']




