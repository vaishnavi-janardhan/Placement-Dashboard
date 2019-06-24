from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dashboard.forms import UserForm, UserProfileInfoForm 


def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def special(request):
    return HttpResponse('You are logged in.')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index')) 
            else:
                return HttpResponseRedirect("Your account was inactive")
        else:
            print("Someone tried to login and failed.")
            print("They used username : {username} and password : {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dashboard/login.html', {})       