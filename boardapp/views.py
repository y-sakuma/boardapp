from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import BoardModel


def signupfunc(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        user_pass = request.POST['password']
        try:
            User.objects.get(user_name)
            return render(request, 'signup.html',
                         {'error': 'This user is already registered.'})
        except:
            user = User.objects.create_user(user_name, '', user_pass)
            return render(request, 'signup.html', {'some': 100})
    return render(request, 'signup.html', {'some': 100})


def loginfunc(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        user_pass = request.POST['password']
        user = authenticate(request, username=user_name, password=user_pass)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    return render(request, 'login.html')


@login_required
def indexfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'index.html', {'object_list': object_list})
