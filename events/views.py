from django.shortcuts import render
from events.models import Event

def events(request):
    event_list = Event.objects.all()
    context_dict = {'events' : event_list, 'navbar' : 'events'}
    return render(request, 'events/events.html', context_dict)
