from django.urls import path
from . import views 

urlpatterns = [
    path('login/',views.signIn ,name='login'),
    path('register/',views.register,name='register'),
    path("logut/",views.logout_view, name="logout")
]
