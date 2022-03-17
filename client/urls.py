from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='cindex'),
    path('about/',views.about,name='about'),
    path('codes/',views.codes,name='codes'),
    path('contact/',views.contact,name='contact'),
    path('treatments/',views.treatments,name='treatments'),
    path('inquiry/',views.inquiry,name='inquiry'),
    path('signin/',views.signin,name='signin'),
    path('book-test/<int:pk>',views.book_test,name='book-test'),
    path('view-test/<int:pk>',views.view_test,name='view-test'),
    path('signup/',views.signup,name='signup'),
    path('cotp/',views.cotp,name='cotp'),


]