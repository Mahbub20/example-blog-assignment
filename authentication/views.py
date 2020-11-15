from django.http import Http404
from django.shortcuts import render, redirect
from authentication.forms import SignUpForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# LOGIN VIEW ENDPOINT

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in!")
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password!')
        else:
            messages.error(request, 'Invalid username or password!')
    form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'login.html', context)

def logout_request(request):
    logout(request)
    messages.info(request, "You are logged out!")
    return redirect('/')


def register(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()    
            return redirect('authentication:login')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form':form})