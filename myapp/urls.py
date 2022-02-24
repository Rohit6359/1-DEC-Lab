from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login,name='login'),
    path('index/', views.index,name='index'),
    path('register/', views.register,name='register'),
    path('otp/', views.otp,name='otp'),
    path('logout/', views.logout,name='logout'),
    path('profile/', views.profile,name='profile'),
    path('icons/', views.icons,name='icons'),
    path('change-password/', views.change_password,name='change-password'),
]
