from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import HttpResponse

class Dog:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Lolo', 'tabby', 'Kinda rude.', 3),
  Dog('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Dog('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Dog('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def dog_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })