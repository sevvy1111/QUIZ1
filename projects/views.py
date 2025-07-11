from django.shortcuts import render
from .models import Project # Import your Project model

def home_page(request):
    projects = Project.objects.all().order_by('-created_at') # Get all projects
    context = {'projects': projects}
    return render(request, 'projects/home.html', context)

def about_page(request):
    return render(request, 'projects/about.html')