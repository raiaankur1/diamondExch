from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("register/", views.signup, name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('deposit', views.deposit, name="deposit"),
    path('withdraw', views.withdraw, name="withdraw"),
]
