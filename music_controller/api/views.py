from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("<h1>Hello</h1>")


# login page
def login(request):
    return HttpResponse("<h2>Welcome to the Login page.</h2>")


