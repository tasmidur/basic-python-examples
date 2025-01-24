from django.db import models

# Create your models here.

class Friends(models.Model):
    GENDER={
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
        
    }
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    gender= models.CharField(max_length=6,choices=GENDER)
    age=models.DecimalField(max_digits=3,decimal_places=2)
    dob = models.DateField(blank=True, null=True)  # New due_date field
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    avater= models.FileField(upload_to='attachments/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
