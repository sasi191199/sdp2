from django.urls import path, include
from . import views

urlpatterns = [

    path('register/',views.register,name="register"),
    path('login/',views.loginpage,name="login"),
    path('myaccount/', views.myaccount, name="myaccount"),
    path('bookevent/', views.bookevent, name="bookevent"),
]
