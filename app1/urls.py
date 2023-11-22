from app1.views import *
from django.urls import path

app_name='n'

urlpatterns=[
    path('first/',first,name='first'),
    path('sec/', sec, name = 'sec'),
]