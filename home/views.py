from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.http import HttpResponse


def my_logout(request):
    logout(request)
    return redirect('home')

#  LECTURE CONTENT
class MyView(TemplateView):
    template_name: str = 'home.html'