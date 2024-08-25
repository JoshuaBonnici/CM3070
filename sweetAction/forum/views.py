from django.shortcuts import render

# Create your views here.

# define the index page view
def index(request):
    return render(request, 'forum/index.html')

def general(request):
    return render(request, 'forum/general.html')

def user_login(request):
    return render(request, 'forum/login.html')

def user_logout(request):
    return render(request, 'forum/logout.html')



def brunch(request):
    return render(request, 'forum/brunch.html')


def suggestionbox(request):
    return render(request, 'forum/suggestionbox.html')

def placeridiculous(request):
    return render(request, 'forum/placeridiculous.html')