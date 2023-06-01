from django.forms import ModelForm
from .models import Nap

class NapForm(ModelForm):
  class Meta:
    model = Nap
    fields = ['date', 'time']