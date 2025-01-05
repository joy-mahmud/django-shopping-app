from django import forms 
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username=forms.CharField()
    password=forms.CharField()
    
class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']
