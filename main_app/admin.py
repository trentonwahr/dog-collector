from django.contrib import admin
from .models import Dog, Nap, Treat

# Register your models here.
admin.site.register(Dog)
admin.site.register(Nap)
admin.site.register(Treat)