from app2.views import *
from django.urls import path

app_name='p'
urlpatterns=[
    path('third/', third, name='third'),
    path('four/', four, name='four')
]