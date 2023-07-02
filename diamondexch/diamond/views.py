from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader


def index(request):
    return render(request, "diamond/Index.html", {})


def home(request):
    template = loader.get_template("diamond/home.html")
    return HttpResponse(template.render({}, request))
