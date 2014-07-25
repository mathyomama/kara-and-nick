from django.contrib import admin
from .models import SelectedThingsToDoEntry, ThingsToDoEntry

# Register your models here.
@admin.register(SelectedThingsToDoEntry)
class SelectedThingsToDoEntryAdmin(admin.ModelAdmin):
	pass

@admin.register(ThingsToDoEntry)
class ThingsToDoEntryAdmin(admin.ModelAdmin):
	pass
