from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='cindex'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('treatments/',views.treatments,name='treatments'),
    path('inquiry/',views.inquiry,name='inquiry'),
    path('signin/',views.signin,name='signin'),
    path('client-logout/',views.client_logout,name='client-logout'),
    path('book-test/<int:pk>',views.book_test,name='book-test'),
    path('view-test/<int:pk>',views.view_test,name='view-test'),
    path('proceed-test/<int:pk>',views.proceed_test,name='proceed-test'),
    path('signup/',views.signup,name='signup'),
    path('cotp/',views.cotp,name='cotp'),


]