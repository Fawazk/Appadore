from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('api/addinterview',views.InterviewList.as_view(),name='interview'), 
    path('api/sheduledinteview/',views.Getsheduledtime.as_view(),name='result'),
]
# http://127.0.0.1:8000/api/sheduledinteview/?id=1&pk=2&date=2022-08-03