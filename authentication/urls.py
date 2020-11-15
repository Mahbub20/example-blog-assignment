from django.urls import path
from authentication.views import login_request, register,logout_request

app_name = 'authentication'

urlpatterns = [
    path('login/', login_request, name='login'),
    path('logout/',logout_request, name='logout'),
    path('register/', register, name='register'),
]
