from django.contrib import admin
from .models import GuestbookEntry

# Register your models here.
@admin.register(GuestbookEntry)
class GuestbookEntryAdmin(admin.ModelAdmin):
	pass
