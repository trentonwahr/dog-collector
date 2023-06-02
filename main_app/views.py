from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dog, Treat
from .forms import NapForm

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def dog_index(request):
  dogs = Dog.objects.filter(user=request.user)
  return render(request, 'dogs/index.html', { 'dogs': dogs })

@login_required
def dog_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  treats_dog_doesnt_have = Treat.objects.exclude(id__in = dog.treats.all().values_list('id'))
  nap_form = NapForm()
  return render(request, 'dogs/detail.html', { 'dog': dog, 'nap_form': nap_form, 'treats': treats_dog_doesnt_have })

class DogCreate(LoginRequiredMixin, CreateView):
  model = Dog
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class DogUpdate(LoginRequiredMixin, UpdateView):
  model = Dog
  fields = ['breed', 'description', 'age']

class DogDelete(LoginRequiredMixin, DeleteView):
  model = Dog
  success_url = '/dogs/'

@login_required
def add_nap(request, dog_id):
  form = NapForm(request.POST)
  if form.is_valid():
    new_nap = form.save(commit=False)
    new_nap.dog_id = dog_id
    new_nap.save()
  return redirect('dog-detail', dog_id=dog_id)

class TreatCreate(LoginRequiredMixin, CreateView):
  model = Treat
  fields = '__all__'

class TreatList(LoginRequiredMixin, ListView):
  model = Treat

class TreatDetail(LoginRequiredMixin, DetailView):
  model = Treat

class TreatUpdate(LoginRequiredMixin, UpdateView):
  model = Treat
  fields = ['name', 'size']

class TreatDelete(LoginRequiredMixin, DeleteView):
  model = Treat
  success_url = '/treat/'

@login_required
def assoc_treat(request, dog_id, treat_id):
  Dog.objects.get(id=dog_id).treats.add(treat_id)
  return redirect('dog-detail', dog_id=dog_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('dog-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)