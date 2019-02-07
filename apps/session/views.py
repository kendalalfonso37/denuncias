from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def SessionView(request):
    return render(request, 'session/session.html')
@login_required
def logoutView(request):
    logout(request)
    return redirect('home')


