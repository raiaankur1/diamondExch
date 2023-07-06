from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import inlineformset_factory
from datetime import datetime, date, timedelta

from .models import *
from .forms import *

import random
from .backends import PhoneUsernameAuthenticationBackend as EoP


def signup(request):
    form = UserCreationForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            print(form.data)
            form = UserCreationForm(request.POST)
            print(form.errors)
            if form.is_valid():
                print("valid form")
                # process the data in form.cleaned_data as required
                cd = form.cleaned_data
                phone_number = cd['phone_number']
                try:
                    get_user_model().objects.get(phone_number=phone_number)
                    messages.error(
                        request, 'An account is already registered with this phone number'
                    )
                    return redirect('login')
                except get_user_model().DoesNotExist:
                    phone_number = cd.get('phone_number')
                    password = cd.get('password')
                    freeGameids = Gameid.objects.filter(user=None)
                    freegid = freeGameids[0]
                    new_user = get_user_model().objects.create_user(
                        phone_number=phone_number, password=password)
                    new_user.gameid = freegid
                    freegid.user = new_user
                    new_user.save()
                    freegid.save()

                    messages.success(
                        request, "Account created for " + f"{phone_number}"
                    )
                    print("account created")
                    return redirect("login")
                # if (len(get_user_model().objects.filter(phone_number=request.POST.get("phone_number"))) != 0):
                #     messages.error(
                #         request, 'An account is already registered with this phone number'
                #     )
                #     return redirect('login')

                # user = form.save()
                # phone_number = form.cleaned_data.get('phone_number')
                # password = form.cleaned_data.get('password')
                # freeGameids = Gameid.objects.filter(user=None)
                # freegid = freeGameids[0]
                # new_user = User(phone_number=phone_number, password=password)
                # new_user.gameid = freegid
                # freegid.user = new_user
                # new_user.save()
                # freegid.save()

                # messages.success(
                #     request, "Account created for " + phone_number
                # )
                # return redirect("login")
            else:
                print("invalid form")
                return redirect("register")

        # if a GET (or any other method) we'll create a blank form
        content = {"form": form}
        return render(request, "diamond/Index.html", content)


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'diamond/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        # print(form.is_valid())
        # cd = form.cleaned_data
        # userr = get_user_model().objects.get(phone_nuber=cd['phone_number'])
        # messages.info(
        #     request, 'Your entered '+cd['phone_number']+'Your registered account is'+userr.__str__(), 'danger')
        if form.is_valid():
            cd = form.cleaned_data
            print(get_user_model().objects.get(
                phone_number=cd['phone_number']).password)
            user = EoP.authenticate(
                request, phone_number=cd['phone_number'], password=cd['password'])
            if user is not None:
                print('logged in')
                login(request, user,
                      backend='django.contrib.auth.backends.ModelBackend')
                messages.success(
                    request, 'You have successfully logged in!', 'success')
                return redirect('home')
            else:
                print('not logged in')
                messages.error(
                    request, 'Your phone number or password is incorrect!', 'danger')
        return render(request, self.template_name, {'form': form})


# def login(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         if request.method == "POST":
#             phone_number = request.POST.get('phone_number')
#             password = request.POST.get('password')

#             user = User.objects.get(phone_number=phone_number)

#             if user is None:
#                 messages.error(
#                     request, "Phone number not registered, kindly register first.")
#                 # messages.error(
#                 #     request, "Registered user is:" + user.__str__())
#                 return render(request, "diamond/login.html", {})

#             user = authenticate(
#                 request, user, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.info(
#                     request, "Username or Password is incorrect. If not registered, kindly register first.")
#         return render(request, "diamond/login.html", {})


def logout_user(request):
    logout(request)
    return redirect('login')


def index(request):
    return render(request, "diamond/Index.html", {})


@login_required(login_url='login')
def deposit(request):
    user = request.user
    phone_number = f"{user.phone_number}"
    balance = user.balance
    content = {
        "phone_number": phone_number,
        "balance": balance,
    }
    return render(request, "diamond/payment.html", content)


@login_required(login_url='login')
def withdraw(request):
    content = {}
    return render(request, "diamond/withdraw.html", content)


@login_required(login_url='login')
def home(request):
    user = request.user
    phone_number = f"{user.phone_number}"
    balance = user.balance
    gameid = user.gameid
    username = gameid.username
    password = gameid.password
    content = {
        "phone_number": phone_number,
        "balance": balance,
        "gameid": username,
        "game_password": password,
    }
    return render(request, "diamond/home.html", content)
