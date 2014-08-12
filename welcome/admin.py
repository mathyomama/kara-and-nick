from django.contrib import admin
from .models import Welcome, WelcomeUpdateEntry

# Register your models here.
@admin.register(Welcome)
class WelcomeAdmin(admin.ModelAdmin):
    pass

@admin.register(WelcomeUpdateEntry)
class WelcomeUpdateEntryAdmin(admin.ModelAdmin):
    pass
