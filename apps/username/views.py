from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(request):

    return render(request, "index/index.html")

def create(request):
    errors = False
    if len(request.POST['name']) < 8:
        messages.error(request, "Username must be longer than 6!")
        errors = True
        return redirect('/')
    if len(request.POST['name']) > 16:
        messages.error(request, "Username must be less than 16!")
        errors = True
        return redirect('/')
    if errors == False:
        User.objects.create(name = request.POST['name'])
        return redirect('/success')

def success(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, "index/success.html", context)

# Create your views here.
