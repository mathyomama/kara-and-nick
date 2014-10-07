from django.contrib import admin

from .models import FontEntry
from .models import ChosenFont

# Register your models here.
@admin.register(FontEntry)
class FontEntryAdmin(admin.ModelAdmin):
    pass

# Register your models here.
@admin.register(ChosenFont)
class ChosenFontAdmin(admin.ModelAdmin):
    list_display = ('font_class','font_entry')
    pass
