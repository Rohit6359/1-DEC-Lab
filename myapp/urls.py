from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login,name='login'),
    path('index/', views.index,name='index'),
    path('register/', views.register,name='register'),
    path('otp/', views.otp,name='otp'),
    path('logout/', views.logout,name='logout'),
]
