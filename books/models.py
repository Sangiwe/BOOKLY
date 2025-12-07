from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):
    WANT_TO_READ = 'WANT'
    READING = 'READING'
    READ = 'READ'
    DROPPED = 'DROPPED'
    STATUS_CHOICES = [
        (WANT_TO_READ, 'Want to Read'),
        (READING, 'Reading'),
        (READ, 'Read'),
        (DROPPED, 'Dropped'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    isbn = models.CharField(max_length=50, blank=True, null=True)
    cover_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=WANT_TO_READ)
    owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
