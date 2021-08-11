from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("about", views.about, name="about"),
    path("contactus", views.contactus, name="contactus"),
    path("prediction", views.predication1, name="prediction"),
]
