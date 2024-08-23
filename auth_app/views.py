from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm, TeacherForm

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
    next = request.GET.get('next')
    if request.method == 'POST':
        form = LoginForm(request.POST)

        print("Post Request Form")
        # print(form)

        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print("User is authenticated")
                login(request, user)

                if user.is_superuser:
                    return redirect('admin-page-name')
                # return redirect(next if next else 'admin-page-name')
                print("Not Admin")
            else:
                print("User is not authenticated")
        else:
            print("Form is invalid")
    else: 
        form = LoginForm()
        print(f"Get Request Form")
        # print(form)

    return render(request, 'auth/login.html', {'form': form})   

@login_required
def admin_view(request):
    return render(request, 'auth/admin.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
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

            if User.objects.filter(username=username).exists():
                messages.WARNING(request, 'Username already exists')
                return redirect('register')
            
            User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=pswd1)
            messages.success(request, 'User Registration Successful')
        else: 
            print(form.errors)
            print(form.non_field_errors())
    else:
        form = UserRegistrationForm()
    return render(request, 'auth/registration.html', {'form': form})

@login_required
def teacher(request):
    user_list = User.objects.exclude(is_superuser=True)
    print(user_list)
    form = TeacherForm()
    print(form)
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            print("Cleaned Data")
            print("*************")
            print(form.cleaned_data)
            print(form)
            print(form.cleaned_data.get('my_image').content_type)
        else: 
            print("Form is Invalid")
            print(request.FILES.get('my_image').content_type)
            print(form.errors)
    return render(request, 'auth/PersonRegistration.html', {'teachers': user_list, 'form': form})
