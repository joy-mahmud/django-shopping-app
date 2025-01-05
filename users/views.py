from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm,RegisterForm
from django.contrib.auth import login ,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def signIn(request):
    if request.method=="POST":
        form = LoginForm(request.POST, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse('invalid credentials')
                
    return render(request,'users/login.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('login')
    else:
        form = RegisterForm() 
          
    return render(request,'users/register.html',{'form':form})

@ login_required
def logout_view(request):
    logout(request)
    return redirect ('login')
