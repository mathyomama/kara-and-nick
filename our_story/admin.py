from django.contrib import admin
from .models import OurStoryEntry

# Register your models here.
@admin.register(OurStoryEntry)
class OurStoryEntryAdmin(admin.ModelAdmin):
    pass
