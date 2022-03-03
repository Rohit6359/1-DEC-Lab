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
    path('add-test/',views.add_test,name='add-test'),
    path('pending-test/',views.pending_test,name='pending-test'),
    path('approve-test/<int:pk>',views.approve_test,name='approve-test'),
    path('reject-test/<int:pk>',views.reject_test,name='reject-test'),
    path('test-status-en/<int:pk>',views.test_status_en,name='test-status-en'),
    path('test-status-dis/<int:pk>',views.test_status_des,name='test-status-dis'),
    path('test-delete/<int:pk>',views.test_delete,name='test-delete'),
]
