from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def SessionView(request):
    return render(request, 'session/session.html')
@login_required
def logoutView(request):
    logout(request)
    return redirect('home')

class profileView(TemplateView):
    template_name = ""

    def post(self, request):
        if request.is_ajax():
            user = User.objects.filter(id=request.user.id).update(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
            response = JsonResponse({'data': 'Profile changes, saved'})
            return response

        else:
            response = JsonResponse({'error':'No ajax request found.'})
            return response

    def get(self, request):
        return render(request, "session/profile.html")