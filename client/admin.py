from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(ClientUser)
# admin.site.register(Inquiry)
# admin.site.register(BookingTest)

@admin.register(ClientUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['fname','email','mobile','aadhar','address']
    
@admin.register(Inquiry)
class UserAdmin(admin.ModelAdmin):
    list_display = ['fullname','email','mobile']
    
@admin.register(BookingTest)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','client','test','book_time','pay_id','pay_verify']