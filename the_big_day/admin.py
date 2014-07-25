from django.contrib import admin
from .models import ItineraryEntry, WhatToExpect

# Register your models here.
@admin.register(ItineraryEntry)
class ItineraryEntryAdmin(admin.ModelAdmin):
	pass

@admin.register(WhatToExpect)
class WhatToExpectAdmin(admin.ModelAdmin):
	pass
