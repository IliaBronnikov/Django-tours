from django.contrib import admin

# Register your models here.
from .models import Departure, Tour


class DepartureAdmin(admin.ModelAdmin):
    pass


class TourAdmin(admin.ModelAdmin):
    pass
