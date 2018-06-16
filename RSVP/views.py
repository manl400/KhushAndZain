from django.shortcuts import render

# Create your views here.

def RSVP(request):
    return render(request, "RSVP/RSVP.html")