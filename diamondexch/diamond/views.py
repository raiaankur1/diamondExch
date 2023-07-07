from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import inlineformset_factory
from datetime import datetime, date, timedelta

import os
from twilio.rest import Client

from .models import *
from .forms import *

import random
from .backends import PhoneUsernameAuthenticationBackend as EoP


def signup1(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        phone_number = request.POST["phone-no"]

        # Set environment variables for your credentials
        # Read more at http://twil.io/secure
        account_sid = "ACf4d8ee728a88e9f02f8cdd0e4c2ffb5e"
        auth_token = "1ac54333561e38bc2431b4373e2d4710"
        verify_sid = "VA9427e1d557678667c828912726495b1a"
        verified_number = phone_number
        print(verified_number)
        client = Client(account_sid, auth_token)
        verification = client.verify.v2.services(verify_sid) \
            .verifications \
            .create(to=verified_number, channel="sms")
        print(verification.status)

        request.session["phone_number"] = phone_number
        return redirect('signup2')
    return render(request, "diamond/signup1.html", {})


def signup2(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        phone_number = request.POST.get("phone-no")
        otp_code = request.POST.get("otp1") + request.POST.get("otp2") + request.POST.get("otp3") + \
            request.POST.get("otp4") + request.POST.get("otp5") + \
            request.POST.get("otp6")

        account_sid = "ACf4d8ee728a88e9f02f8cdd0e4c2ffb5e"
        auth_token = "1ac54333561e38bc2431b4373e2d4710"
        verify_sid = "VA9427e1d557678667c828912726495b1a"
        verified_number = phone_number

        client = Client(account_sid, auth_token)
        verification_check = client.verify.v2.services(verify_sid) \
            .verification_checks \
            .create(to=verified_number, code=otp_code)
        print(verification_check.status)

        return redirect('signup3')
    try:
        phone_number = request.session["phone_number"]
    except:
        return redirect('signup1')
    content = {
        "phone_number": phone_number,
    }
    return render(request, "diamond/signup2.html", content)


def signup3(request):
    # form = UserCreationForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            # print(form.data)
            # form = UserCreationForm(request.POST)
            # print(form.errors)
            # if form.is_valid():
            print("valid form")
            # process the data in form.cleaned_data as required
            # cd = form.cleaned_data
            phone_number = request.POST.get('phone_number')
            try:
                get_user_model().objects.get(phone_number=phone_number)
                messages.error(
                    request, 'An account is already registered with this phone number'
                )
                return redirect('login')
            except get_user_model().DoesNotExist:
                # phone_number = cd.get('phone_number')
                password = request.POST.get('password1')
                Cpassword = request.POST.get('password2')

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
            # else:
            #     print("invalid form")
            #     return redirect("register")

        # to handle GET method
        try:
            phone_number = request.session["phone_number"]
        except:
            return redirect('signup1')
        content = {
            "phone_number": phone_number,
        }
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
            # print(get_user_model().objects.get(
            #     phone_number=cd['phone_number']).password)
            user = EoP.authenticate(
                request, phone_number=cd['phone_number'], password=cd['password'])
            if user is not None:
                # print('logged in')
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
    messages.info(
        request, "You have been logged out!"
    )
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
    if request.method == "POST":
        # print(get_user_model().objects.get(
        #     phone_number=cd['phone_number']).password)
        try:
            amount = request.POST.get('deposit_amount')
            utr_no = request.POST.get('utr_no')
            # reupi = request.POST.get('reupi')
            # password = request.POST.get('password')
            dStatement = Depositstatement(
                user=user, amount=amount, utrno=utr_no)
            dStatement.save()

            return redirect('depositstatements')
        except:
            return render(request, "diamond/payment.html", content)

    return render(request, "diamond/payment.html", content)


@login_required(login_url='login')
def withdraw(request):
    user = request.user
    phone_number = f"{user.phone_number}"
    balance = user.balance
    content = {
        "phone_number": phone_number,
        "balance": balance,
    }
    if request.method == "POST":
        # print(get_user_model().objects.get(
        #     phone_number=cd['phone_number']).password)
        try:
            amount = request.POST.get('withdraw_amount')
            upi = request.POST.get('upi')
            reupi = request.POST.get('reupi')
            # password = request.POST.get('password')
            wStatement = Withdrawstatement(user=user, amount=amount, upiid=upi)
            wStatement.save()

            return redirect('withdrawstatements')
        except:
            return render(request, "diamond/withdrawForm.html", content)

    return render(request, "diamond/withdrawForm.html", content)


@login_required(login_url='login')
def depositStatements(request):
    user = request.user
    phone_number = f"{user.phone_number}"
    balance = user.balance
    deposit_statements = list(Depositstatement.objects.filter(
        user=user).order_by('-created_at'))
    content = {
        "phone_number": phone_number,
        "balance": balance,
        "deposit_statements": deposit_statements,
    }
    return render(request, "diamond/depositStatements.html", content)


@login_required(login_url='login')
def withdrawStatements(request):
    user = request.user
    phone_number = f"{user.phone_number}"
    balance = user.balance
    withdraw_statements = list(Withdrawstatement.objects.filter(
        user=user).order_by('-created_at'))
    content = {
        "phone_number": phone_number,
        "balance": balance,
        "withdraw_statements": withdraw_statements,
    }
    return render(request, "diamond/withdrawStatements.html", content)


@login_required(login_url='login')
def home(request):
    user = request.user
    phone_number = f"{user.phone_number}"
    balance = user.balance
    try:
        gameid = user.gameid
        username = gameid.username
        password = gameid.password
    except:
        username = "GameID-Username"
        password = "GameID-Password"

    content = {
        "phone_number": phone_number,
        "balance": balance,
        "gameid": username,
        "game_password": password,
    }
    return render(request, "diamond/home.html", content)
