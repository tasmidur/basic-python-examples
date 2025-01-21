from django.contrib import admin
from .models import Todo
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.html import format_html


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority','is_completed','date', 'attachment_preview','created_at', 'updated_at')  # Include due_date in the list view
    search_fields = ('title', 'description')
    list_filter = ('is_completed','priority', 'date')  # Add due_date to the filter options
    ordering = ('-created_at',)
    list_per_page=10
    
    def attachment_preview(self, obj):
        """Return a thumbnail of the attachment if it's an image."""
        if obj.attachment:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.attachment.url)
        return "No Attachment"
    
    attachment_preview.short_description = 'Attachment Preview'  # Column header in the admin

    
     # Define the custom action
    actions = ['mark_as_completed']

    def mark_as_completed(self, request, queryset):
        """Mark selected Todo items as completed."""
        updated_count = queryset.update(is_completed=True)  # Assuming you have an is_completed field
        self.message_user(request, f"{updated_count} Todo items marked as completed.")
    
    mark_as_completed.short_description = "Mark selected Todo items as completed"
    
     # Organizing fields in the edit form
    fieldsets = (
        ("Basic Info", {
            'fields': ('title', 'description','priority','date'),
            'classes':('collapse',)
        }),
        ('Attachments', {
            'fields': ('attachment',),
            'classes': ('collapse',),
        }),
    )
    
    class Media:
        css = {
            'all': (staticfiles_storage.url('myapp/css/admin_custom.css'),)
        }

admin.site.register(Todo, TodoAdmin)