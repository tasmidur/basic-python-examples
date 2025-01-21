from django.db import models

class Todo(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the task is updated
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)  # Field for file attachments
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')  # Priority field


    def __str__(self):
        return self.title