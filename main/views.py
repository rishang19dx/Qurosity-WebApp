from django.shortcuts import render
from .models import Event, TeamMember, Trivia

def events(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'main/events.html', {'events': events})

def homepage(request):
    return render(request, 'main/homepage.html')

def trivia(request):
    return render(request, 'main/trivia.html')

def team(request):
    return render(request, 'main/team.html')

def contact(request):
    return render(request, 'main/contact.html')
