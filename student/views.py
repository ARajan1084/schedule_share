from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from student.forms import UserLoginForm
from student.forms import CreateAccountForm
from django.contrib.auth.models import User
from student.models import Student


def home(request):
    # fetch friendships, and friend requests
    # process request, and create any friend requests
    # fetch friend requests, process accepting and declining
    return render(request, 'student/home.html')


def add_class(request):

    return


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                return redirect('home')
            else:
                messages.error(request, 'Invalid Username or Password')
        else:
            messages.error(request, 'Form is Invalid')
    return render(request, 'student/login.html', {'form': UserLoginForm()})


def create_account(request):
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')
            if password == confirm_password:
                user = User(username=username, email=email)
                user.set_password(password)
                student = Student(user=user, first_name=first_name, last_name=last_name)
                user.save()
                student.save()
                return redirect('login')
            else:
                messages.error(request, 'Passwords do not match')
    return render(request, 'student/create_account.html', {'form': CreateAccountForm()})
