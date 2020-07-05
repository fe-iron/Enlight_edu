from django.shortcuts import render, redirect
from .models import News, UpcomingEvent
from django.contrib.auth.models import auth, User
from django.contrib import messages


# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pass1 = request.POST['password']

        user = auth.authenticate(username=uname, password=pass1)
        if user is not None:
            auth.login(request, user)
            messages.info(request, "Successfully Logged in ")
            return redirect('/')

        else:
            messages.info(request, 'Invalid user id and password')
            return redirect('login')

    else:
        return render(request, 'login.html')


def contact(request):

    if request.method == 'POST':

        fullname = request.POST['fullname']
        uname = request.POST['uname']
        dob = request.POST['dob']
        mob = request.POST['mob']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 == pass2:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username already taken")
                return redirect('contact')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email is already registered")
                return redirect('contact')

            else:
                user = User.objects.create_user(username=uname, password=pass1, email=email)
                user.save()
                messages.info(request, "User account successfully created")
                return redirect('/')

    else:

        return render(request, 'contact.html')


def index(request):
    nws = News.objects.all()
    upcvnt = UpcomingEvent.objects.all()

    return render(request, 'index.html', {'news': nws, 'event': upcvnt})