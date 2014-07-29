from django.contrib import admin
from .models import AccommodationsEntry

# Register your models here.
@admin.register(AccommodationsEntry)
class AccommodationsEntryAdmin(admin.ModelAdmin):
	pass
