from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
import bcrypt
# Create your views here.

def main(request):
    return render(request, 'base/main.html')

class LoginView(TemplateView):
    template_name = "main.html"

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('logged_in')
        else:
            messages.add_message(request, messages.ERROR, 'Error, something went wrong')
            return render(request, 'user/login.html')

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('logged_in')
        return render(request, "user/login.html")

class Signup(TemplateView):
    template_name="user/login.html"

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password  = request.POST['password']
        if 'superuser' in request.POST:
            superuser = True
        else:
            superuser = False

        try:
            u = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password, is_superuser=superuser)
            if u:
                u.save()
                messages.add_message(request, messages.INFO, 'User created.')
                return render(request, "user/signup.html")
            else:
                messages.add_message(request, messages.INFO, 'This user already exists.')
                return render(request, "user/signup.html")
        except:
            messages.add_message(request, messages.WARNING, 'May be the username already exists')
            return render(request, "user/signup.html")
    
    def get(self, request):
        return render(request, "user/signup.html")