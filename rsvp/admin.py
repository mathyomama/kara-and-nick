from django.contrib import admin
from .models import Account, Person

# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
	pass

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	pass
