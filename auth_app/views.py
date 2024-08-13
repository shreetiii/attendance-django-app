from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm

# Create your views here.

# def login(request):
#     if request.method == 'POST':
#         print(request.POST)
#         username = request.POST .get('username')
#         password = request.POST .get('password')
#         print("*******")
#         print(username, password)
#         user = authenticate(username=username, password=password)
#         print(user)
#         if user is None:
#             messages.warning(request, 'Invalid Username or Password')
#             messages.warning(request, 'Please try again')

#     return render(request, 'auth/login.html')

def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print("Post request form")
        print(form)

        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print("User is authenticated")
                login(request, user)
                return redirect('admin-page-name')
            else:
                print("User is not authenticated")
        else:
            print("Form is invalid")
            print(form.non_field_errors())

    else: 
        form = LoginForm()
        print(f"Get Request Form")
        print(form)

    print("Get Request Form")

    return render(request, 'auth/login.html', {'form': form}) 

def admin_view(request):
    return render(request, 'auth/admin.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            pswd1 = form.cleaned_data.get('password1')
            pswd2 = form.cleaned_data.get('password2')
            if pswd1 == pswd2:
                User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=pswd1)
        else: 
            print(form.errors)
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/registration.html', {'form': form})
