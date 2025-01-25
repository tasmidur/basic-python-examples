from django.shortcuts import render
from .models import Friends

# Create your views here.
def home(request):
    friends = Friends.objects.all().order_by("-created_at")  # Corrected this line
    context = {
        'friends': friends
    }
    return render(request, 'home.html', context)