from django.contrib import admin
from .models import PartyMember

# Register your models here.
@admin.register(PartyMember)
class PartyMemberAdmin(admin.ModelAdmin):
    pass
