from django.contrib import admin
from .models import Andamio

# Register your models here.

class AndamioAdmin(admin.ModelAdmin):
    list_per_page = 20

admin.site.register(Andamio, AndamioAdmin)