from django.shortcuts import render
from django.shortcuts import redirect

def nav(request):
    return render(request, "pages/nav.html")

def home(request):
    return render(request, "pages/home.html")
def about(request):
    return render(request, "pages/about.html")
def project(request):
    return render(request, "pages/project.html")
def contact(request):
    return render(request, "pages/contact.html")


