from django.contrib import admin

# Register your models here.

from .models import Room
from .models import DataFromRoom

admin.site.register(Room)
admin.site.register(DataFromRoom)
