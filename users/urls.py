from django.urls import path
from . import views 

urlpatterns = [
    path('login/',views.signIn ,name='login'),
    path("logut/",views.logout_view, name="logout")
]
