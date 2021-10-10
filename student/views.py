from django.shortcuts import render


def home(request):
    return render(request, 'student/home.html')


def login(request):
    return render(request, 'student/login.html')