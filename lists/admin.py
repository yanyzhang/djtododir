from django.contrib import admin

# Register your models here.
from .models import Lists
from .models import Todolistmdl

admin.site.register(Lists)

admin.site.register(Todolistmdl)