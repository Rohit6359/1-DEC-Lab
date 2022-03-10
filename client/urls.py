from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='cindex'),
    path('about',views.about,name='about'),
    path('codes',views.codes,name='codes'),
    path('contact',views.contact,name='contact'),
    path('treatments',views.treatments,name='treatments'),

]