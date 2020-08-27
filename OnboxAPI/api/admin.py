from django.contrib import admin

# Register your models here.

from .models import Lockers, Boxs

admin.site.register(Lockers)
admin.site.register(Boxs)