from django.db import models

# User Model (Basic Info)
class User(models.Model):
    """
    Represents a user in the system with basic personal information.

    Attributes:
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        profile_picture (ImageField): An optional profile picture for the user.
        date_of_birth (DateField): The user's date of birth.
        bio (TextField): An optional biography or description of the user.
        created_at (DateTimeField): The timestamp when the user was created.
        updated_at (DateTimeField): The timestamp when the user was last updated.
    """
    first_name = models.CharField(max_length=100)  # User's first name
    last_name = models.CharField(max_length=100)   # User's last name
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)  # Profile picture upload
    date_of_birth = models.DateField()  # User's date of birth
    bio = models.TextField(blank=True, null=True)  # Optional biography
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update

    def __str__(self):
        return f"{self.first_name} {self.last_name}"  # String representation of the user

# Education Model
class Education(models.Model):
    """
    Represents an educational qualification of a user.

    Attributes:
        user (ForeignKey): The user associated with this education record.
        degree (str): The degree obtained by the user.
        institution_name (str): The name of the institution where the degree was obtained.
        field_of_study (str): The field of study for the degree (optional).
        start_date (DateField): The start date of the education.
        end_date (DateField): The end date of the education (optional).
        description (TextField): A description of the education (optional).
        created_at (DateTimeField): The timestamp when the education record was created.
        updated_at (DateTimeField): The timestamp when the education record was last updated.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="educations")  # Link to User model
    degree = models.CharField(max_length=100)  # Degree obtained
    institution_name = models.CharField(max_length=200)  # Name of the institution
    field_of_study = models.CharField(max_length=100, blank=True, null=True)  # Field of study (optional)
    start_date = models.DateField()  # Start date of education
    end_date = models.DateField(blank=True, null=True)  # End date of education (optional)
    description = models.TextField(blank=True, null=True)  # Description of the education (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update

    def __str__(self):
        return f"{self.degree} - {self.institution_name}"  # String representation of the education record

# Experience Model
class Experience(models.Model):
    """
    Represents a work experience of a user.

    Attributes:
        user (ForeignKey): The user associated with this experience record.
        job_title (str): The title of the job held by the user.
        company_name (str): The name of the company where the user worked.
        start_date (DateField): The start date of the job.
        end_date (DateField): The end date of the job (optional).
        description (TextField): A description of the job responsibilities (optional).
        created_at (DateTimeField): The timestamp when the experience record was created.
        updated_at (DateTimeField): The timestamp when the experience record was last updated.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="experiences")  # Link to User model
    job_title = models.CharField(max_length=100)  # Job title
    company_name = models.CharField(max_length=200)  # Company name
    start_date = models.DateField()  # Start date of the job
    end_date = models.DateField(blank=True, null=True)  # End date of the job (optional)
    description = models.TextField(blank=True, null=True)  # Description of job responsibilities (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update

    def __str__(self ):
        return f"{self.job_title} at {self.company_name}"  # String representation of the experience record

# ContactInformation Model
class ContactInformation(models.Model):
    """
    Represents the contact information of a user.

    Attributes:
        user (ForeignKey): The user associated with this contact information.
        phone_number (str): The user's phone number (optional).
        email (EmailField): The user's email address.
        address (TextField): The user's physical address (optional).
        created_at (DateTimeField): The timestamp when the contact information was created.
        updated_at (DateTimeField): The timestamp when the contact information was last updated.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="contact_info")  # Link to User model
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Phone number (optional)
    email = models.EmailField(unique=True)  # User's email address
    address = models.TextField(blank=True, null=True)  # Physical address (optional)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update

    def __str__(self):
        return f"Contact Info for {self.user.first_name} {self.user.last_name}"  # String representation of contact information ```python

 