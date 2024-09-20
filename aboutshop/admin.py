from django.contrib import admin
from .models import Aboutshop


@admin.register(Aboutshop)
class AboutshopAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    list_editable = ['description']