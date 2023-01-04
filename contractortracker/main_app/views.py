from django.shortcuts import render
from re import template
from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Client, Task
from .forms import TaskForm, CustomUserCreationForm

# Create your views here.
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print(form)
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid signup. Please try again. Sorry!'

    form = CustomUserCreationForm()
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)

def client_index(request):
    clients = Client.objects.all
    return render(request, 'clients/index.html', {'clients': clients})

def home(request):
    return render(request, "home.html")

# def signup(request):
#     error_message = ''
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index')
#         else:
#             error_message = 'Invalid signup. Sorry!!! Try again.'
#     form = UserCreationForm()
#     context = {
#         'form': form,
#         'error_message': error_message
#     }
#     return render (request, 'registration/signup.html', context)

class NewClient(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['name', 'address1', 'address2', 'city', 'state', 'zip_code']
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse('index')

def manage_client(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request, 'clients/manage.html', {'client': client})

def add_task(request, client_id):
    form = TaskForm(request.POST)
    client = Client.objects.get(id=client_id)
    if form.is_valid():
        new_task = form.save(commit=False)
        new_task.client_id = client.id
        new_task.completed = True
        # this is where new_recipe.user = request.user would be for pourspot
        new_task.save()
        client = Client.objects.get(id=client_id)
        return render(request, 'clients/manage.html', {'client': client})
    return render(request, 'main_app/task_form.html', {'form': form, 'client': client})
