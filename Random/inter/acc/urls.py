from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.front),
    path('customer/',views.main_customers,name="cust"),
    path('new/',views.new),
    path('logined/', views.loginPage,name="login"),
    path('logout/', views.logoutUser,name="logout"),
    path('register/', views.registerPage),
]