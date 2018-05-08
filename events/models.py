from django.db import models

class Event(models.Model):
    NewYork = 'New York City, NY'
    Normal = 'Normal, IL'
    Karachi = 'Karachi, Pakistan'
    LOCATIONS = (
        (NewYork, 'New York City, NY'),
        (Normal, 'Normal, IL'),
        (Karachi, 'Karachi, Pakistan')
    )

    title = models.CharField(max_length=30)
    description = models.TextField()
    location = models.CharField(max_length=30, choices=LOCATIONS, default=NewYork)
    address = models.CharField(max_length=140)
    timeline = models.TextField()
    dressCode = models.TextField()
    duration = models.DurationField()
    date = models.DateTimeField()
    
    def __str__(self):
        return self.title