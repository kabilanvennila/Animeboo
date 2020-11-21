from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect


# Create your views here.

def Signup(request):
    if request.method == "POST":
        signupForm=UserCreationForm(request.POST)
        if signupForm.is_valid():
            USER=signupForm
            USER.save()
            messages.success(request,f'Yayy! Welcome ,Your account has been created sucessfully Login to continue')
            return redirect(reverse('Login'))   
    signup_form=UserCreationForm()
    return render(request,'authentication/Signup.html',{"signup_form":signup_form})


def login(request):  
    if request.method == "POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,
            password=password)
            return redirect('home')
            #return redirect(reverse('home'))
        else:
            messages.info(request,'Invalid Credentials')
            return redirect(reverse('Login'))               
    Login_form=AuthenticationForm()
    return render(request,'authentication/Login.html',{"Login_form":Login_form})
     

def logout(request):
    return render(request,'authentication/logout.html')
