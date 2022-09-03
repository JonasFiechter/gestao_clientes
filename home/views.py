from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')

#  LECTURE CONTENT
class MyView(TemplateView):
    template_name: str = 'home.html'

    def post(self, request):
        return HttpResponse('WORKING')

    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        return {'VAR': 'TESTING TEMPLATE VIEW WITH DICTS'}

#  LECTURE CONTENT
class MyView2(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home2.html')

    def post(self, request, *args, **kwargs):
        a = request.POST.get('input')
        print(a)
        return render(request, 'home2.html')
