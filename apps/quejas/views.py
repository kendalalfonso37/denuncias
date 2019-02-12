from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from apps.quejas.models import Queja
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
class QuejasView(TemplateView):
    template_name = ""

    def get(self, request):
        quejas = Queja.objects.all()
        return render(request, "quejas/queja.html", {'queja':quejas})

    def post(self, request):
        return render(request, "quejas/queja.html")
        