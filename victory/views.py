from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(Request):
    return render(Request,"base.html")
def about(Request):
    return render(Request,"about.html")
def projects(Request):
    return render(Request, "projects.html")
def contact(Request):
    return render(Request, "contact.html")

