from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("register/", views.signup, name="register"),
    path("login/", views.login, name="login"),
    path('logout/', views.logout_user, name="logout"),
]
