from pyexpat import model
from typing import List
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Person
from .forms import PersonForm


@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})


@login_required
def persons_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})


class MyView3(ListView):
    model = Person
    template_name: str = 'person_list.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        my_list = context['object_list']
        print(my_list)
        return context


class MyView4(DetailView):
    model = Person
    template_name: str = 'clientes/person_detail.html'


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        my_object = context['object']
        print(my_object)
        return context

class MyView5(CreateView):
    model = Person
    template_name: str = 'clientes/person_create.html'
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/clientes/person_list'


class MyView6(UpdateView):
    model = Person
    template_name = 'clientes/person_update.html'
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/clientes/person_list'