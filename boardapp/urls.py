from django.urls import path, include

from .views import topfunc, signupfunc, loginfunc, logoutfunc, indexfunc, detailfunc, goodfunc
from .views import BoardCreate


urlpatterns = [
    path('', topfunc, name='top'),
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('logout/', logoutfunc, name='logout'),
    path('index/', indexfunc, name='index'),
    path('detail/<int:pk>/', detailfunc, name='detail'),
    path('good/<int:pk>/', goodfunc, name='good'),
    path('create/', BoardCreate.as_view(), name='create'),
]