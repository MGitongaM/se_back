from django.contrib import admin
from .models import *

# Register your models here.
class UserA(admin.ModelAdmin):
    list_display = ('email','is_active','is_superuser')
    list_filter = ('date_created','is_superuser')

admin.site.register(UserAccount,UserA)
