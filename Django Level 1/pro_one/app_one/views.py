from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_me':"Hello! I'm from views.py"}
    return render(request, "app_one/index.html", context = my_dict)
    #return HttpResponse("<em>My Second App</em>")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request, 'app_one/help.html', context= helpdict)