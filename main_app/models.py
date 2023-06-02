from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

TIMES = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('N', 'Night')
)

class Treat(models.Model):
  name = models.CharField(max_length=50)
  size = models.CharField(max_length=20)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("treat-detail", kwargs={"pk": self.id})

class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  treats = models.ManyToManyField(Treat)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("dog-detail", kwargs={"dog_id": self.id})
  
  def napped_for_today(self):
    return self.nap_set.filter(date=date.today()).count() >= len(TIMES)
  
class Nap(models.Model):
  date = models.DateField('Nap date')
  time = models.CharField(
    max_length=1,
    choices=TIMES,
    default=TIMES[0][0]
  )

  dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_time_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']