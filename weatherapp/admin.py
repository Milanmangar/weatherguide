from django.contrib import admin

# Register your models here.
from .models import City,CityUser

admin.site.register(City)
admin.site.register(CityUser)
