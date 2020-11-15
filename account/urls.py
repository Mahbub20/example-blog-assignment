from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi

app_name = 'account'

urlpatterns = [
    path('api/register', RegisterApi.as_view()),
]