from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import User

def personal_profile(request):
    user = get_object_or_404(User, id=1)
    context = {
        'user': user,
        'educations': user.educations.all(),
        'experiences': user.experiences.all(),
        'contact_info': user.contact_info,
    }
    print(context)
    return render(request, 'personal_app/public_profile.html', context)

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Ensure you have a home.html template
