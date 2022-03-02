from django.shortcuts import render, redirect
# Create your views here.

def home(request):
    return redirect('add_order/')#render(request, "main/main.html")