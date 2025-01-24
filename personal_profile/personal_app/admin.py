from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Education, Experience, ContactInformation

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'bio','profile_picture')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution_name', 'start_date', 'end_date')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name', 'start_date', 'end_date')

@admin.register(ContactInformation)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'address')
