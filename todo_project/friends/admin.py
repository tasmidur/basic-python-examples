from django.contrib import admin

from .models import Friends

# Register your models here.

class FriendsAdmin(admin.ModelAdmin):
    # list of value
    list_display = ('name', 'email', 'phone', 'dob','avater','created_at')
    list_per_page=2
    search_fields=('name','email','phone')
    list_filter=('name', 'email', 'phone', 'dob','avater','created_at')
    ordering = ('-created_at',)

   

admin.site.register(Friends, FriendsAdmin)