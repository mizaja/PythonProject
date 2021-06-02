from django.urls import path
from . import  views

app_name='searchap'

urlpatterns=[
    path('',views.searchresult,name='searchresult'),

]