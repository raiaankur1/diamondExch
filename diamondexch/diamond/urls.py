from django.urls import path

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("signup/", views.signup1, name="signup1"),
    path("verify/<str:uid>/", views.signup2, name="signup2"),
    path("register/<str:uid>/", views.signup3, name="signup3"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('deposit', views.deposit, name="deposit"),
    path('withdraw', views.withdraw, name="withdraw"),
    path('depositStatements', views.depositStatements, name="depositstatements"),
    path('withdrawStatements', views.withdrawStatements, name="withdrawstatements"),
]
