from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm
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

@ login_required
def logout_view(request):
    logout(request)
    return redirect ('login')
