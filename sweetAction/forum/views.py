from django.shortcuts import render

# Create your views here.

# define the index page view
def index(request):
    return render(request, 'forum/index.html')