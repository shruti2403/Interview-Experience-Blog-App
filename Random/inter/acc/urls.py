from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.front),
    path('customer/',views.main_customers,name="cust"),
    path('new/',views.new),
    path('logined/', views.loginPage),
    path('register/', views.registerPage),
]