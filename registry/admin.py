from django.contrib import admin
from .models import RegistryEntry

# Register your models here.
@admin.register(RegistryEntry)
class RegistryEntryAdmin(admin.ModelAdmin):
	pass
