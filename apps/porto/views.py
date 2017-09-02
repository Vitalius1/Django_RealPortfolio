from django.shortcuts import render

def index(request):
    return render(request, "porto/index.html")

def showProjects(request):
    return render(request, "porto/projects.html")

def showAbout(request):
    return render(request, "porto/about.html")

def showTestimonials(request):
    return render(request, "porto/testimonials.html")

# Create your views here.
