from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Project, Image

def index(request):
    return render(request, "portfolio/index.html")

def mobile(request):
    context = {
        "projects": Project.objects.filter(category="mobile"),
        "images": Image.objects.filter(category="mobile")
    }
    return render(request, "portfolio/project.html", context)

def apps(request):
    context = {
        "projects": Project.objects.filter(category="web"),
        "images": Image.objects.filter(category="web")
    }
    return render(request, "portfolio/project.html", context)

def sites(request):
    return render(request, "portfolio/index.html")

def graphic(request):
    return render(request, "portfolio/index.html")

def blog(request):
    return render(request, "portfolio/blog.html")

def contact(request):
    return render(request, "portfolio/contact.html")

def error(request):
    context = {
        "message": "This is an error message"
    }
    return render(request, "portfolio/error.html", context)
