from django.contrib import admin

from .models import Friends

# Register your models here.

class FriendsAdmin(admin.ModelAdmin):
    # list of value
    list_display = ('name', 'email', 'phone', 'dob','avater','created_at')
   

admin.site.register(Friends, FriendsAdmin)