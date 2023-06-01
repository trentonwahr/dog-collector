from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dog
from .forms import NapForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dog_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', { 'dogs': dogs })

def dog_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  nap_form = NapForm()
  return render(request, 'dogs/detail.html', { 'dog': dog, 'nap_form': nap_form })

class DogCreate(CreateView):
  model = Dog
  fields = ['name', 'breed', 'description', 'age']

class DogUpdate(UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'

def add_nap(request, dog_id):
  form = NapForm(request.POST)
  if form.is_valid():
    new_nap = form.save(commit=False)
    new_nap.dog_id = dog_id
    new_nap.save()
  return redirect('dog-detail', dog_id=dog_id)