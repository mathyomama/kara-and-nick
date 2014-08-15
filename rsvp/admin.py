from django.contrib import admin
from .models import Account, Person
from django.contrib.auth.models import Group

# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        Group.objects.get(name='Guest').user_set.add(obj)
        obj.save()

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
