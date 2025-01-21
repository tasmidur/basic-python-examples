from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'complete', 'priority', 'created_at', 'updated_at')
    list_filter = ('complete', 'priority')
    search_fields = ('title',)
    ordering = ('-created_at',)  # Order by created_at descending

admin.site.register(Todo, TodoAdmin)