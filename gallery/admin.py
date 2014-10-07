from django.contrib import admin
from .models import GalleryEntry

# Register your models here.
@admin.register(GalleryEntry)
class GalleryEntryAdmin(admin.ModelAdmin):
    pass

#@admin.register(GalleryUploadEntry)
#class GalleryUploadEntryAdmin(admin.ModelAdmin):
#    pass
