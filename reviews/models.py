from django.db import models
from django.contrib.auth import get_user_model
from books.models import Book

User = get_user_model()

class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user','book')  # optional: one review per user per book

    def __str__(self):
        return f"Review {self.rating} by {self.user} for {self.book}"
