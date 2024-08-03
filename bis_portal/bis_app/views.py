from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.

#These are functions
def dashboard(request):
    return render(request,"index.html", context={})

def shopping(request):
    return HttpResponse("Welcome to shopping")    

def save_member(request):
    member_name = request.POST['member_name']
    #return HttpResponse("Welcome to Book Library - "+ member_name) #will retrieve name typed on the web and displayed on the web
    return render(request,"welcome.html", context={'member_name':member_name})