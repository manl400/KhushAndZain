from django.db import models

class Post(models.Model):
    Khushi = 'Khushi'
    Zain = 'Zain'
    AUTHOR_CHOICES = (
        (Khushi, 'Khushi'),
        (Zain, 'Zain')
    )

    title = models.CharField(max_length=140)
    body = models.TextField()
    author = models.CharField(max_length=10, choices=AUTHOR_CHOICES, default=Zain)
    date = models.DateTimeField()

    def __str__(self):
        return self.title