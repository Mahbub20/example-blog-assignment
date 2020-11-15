from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import MyUser

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    #email = forms.EmailField(max_length=40)
    #User._meta.get_field('username')._unique = False
    #USERNAME_FIELD = 'email'

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if MyUser.objects.filter(email=data).count()>0:
            raise forms.ValidationError("Already have a user registered with this email-address.")
        return data