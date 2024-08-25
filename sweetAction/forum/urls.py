# import the necessary libraries
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.contrib.auth.decorators import login_required

from . import views


# setup the url paths for the endpoints and index
urlpatterns = [
    path('', views.index, name='index'),
    path('general.html', views.general, name='general'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('brunch.html', views.brunch, name='brunch'),
    path('suggestionbox.html', views.suggestionbox, name='suggestionbox'),
    path('placeridiculous.html', views.placeridiculous, name='placeridiculous'),]

    # # example url path for a page that can only be viewed via login.
    # # Having the below sends the user to the login page if they try to click the link without being logged in
    # path('logout/', login_required(login_url='../login/')(views.user_logout), name='logout'),