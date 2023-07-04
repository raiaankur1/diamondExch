from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import inlineformset_factory
from datetime import datetime, date, timedelta

from .models import *
from .forms import *


def signup(request):
    form = UserCreationForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                # process the data in form.cleaned_data as required
                if (len(User.objects.filter(phone_number=request.POST.get("phone_number"))) != 0):
                    messages.error(
                        request, 'An account is already registered with this phone number'
                    )
                    return redirect('login')

                # user = form.save()
                phone_number = form.cleaned_data.get('phone_number')
                password = form.cleaned_data.get('password')
                freeGameids = Gameid.objects.filter(user=None)
                freegid = freeGameids[0]
                new_user = User(phone_number=phone_number, password=password)
                new_user.gameid = freegid
                freegid.user = new_user
                new_user.save()
                freegid.save()

                messages.success(
                    request, "Account created for " + phone_number
                )
                return redirect("login")

            return redirect("")

        # if a GET (or any other method) we'll create a blank form
        content = {"form": form}
        return render(request, "diamond/otp.html", content)


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            phone_number = request.POST.get('phone_number')
            password = request.POST.get('password')

            user = authenticate(
                request, phone_number=phone_number, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(
                    request, "Username or Password is incorrect. If not registered, kindly register first.")
        return render(request, "diamond/login.html", {})


def logout_user(request):
    logout(request)
    return redirect('login')


def index(request):
    return render(request, "diamond/Index.html", {})


def home(request):
    template = loader.get_template("diamond/home.html")
    return HttpResponse(template.render({}, request))
