from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import BoardModel

def topfunc(request):
    return render(request, 'top.html')


def signupfunc(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        user_pass = request.POST['password']
        try:
            User.objects.get(username=user_name)
            return render(request, 'signup.html',
                         {'error': 'This user is already registered.'})
        except:
            user = User.objects.create_user(user_name, '', user_pass)
            return redirect('login')
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


def logoutfunc(request):
    logout(request)
    return redirect('login')


@login_required
def indexfunc(request):
    object_list = BoardModel.objects.all()
    return render(request, 'index.html', {'object_list': object_list})


def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})


def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    login_user = request.user.get_username()
    if login_user not in post:
        post.read += 1
        post.readtext = post.readtext + ' ' + login_user
        post.save()
    else:
        pass


class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'author', 'images')
    success_url = reverse_lazy('index')
