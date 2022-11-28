from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name="loginpage"),
    path('create-user/', views.createuser, name="createuser"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.logout, name="logout")
]