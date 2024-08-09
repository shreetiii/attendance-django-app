from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.

def login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST .get('username')
        password = request.POST .get('password')
        print("*******")
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            messages.warning(request, 'Invalid Username or Password')

    return render(request, 'auth/login.html')
