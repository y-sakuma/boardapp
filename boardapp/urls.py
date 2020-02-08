from django.urls import path, include

from .views import signupfunc, loginfunc, indexfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('', loginfunc, name='login'),
    path('index/', indexfunc, name='index'),
    path
]