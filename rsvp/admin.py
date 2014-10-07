from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import Account, Person, Image

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass
    
#    def save_model(self, request, obj, form, change):
#        Group.objects.get(name='Guest').user_set.add(obj)
#        obj.save()

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('account', 'first_name', 'last_name')

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
