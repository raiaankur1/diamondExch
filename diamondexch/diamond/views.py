from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from .forms import *


def index(request):
    return render(request, "diamond/Index.html", {})


def home(request):
    template = loader.get_template("diamond/home.html")
    return HttpResponse(template.render({}, request))


def login(request):
    loginForm = UserCreationForm()
    content = {"form": loginForm}
    return render(request, "diamond/login.html", content)
