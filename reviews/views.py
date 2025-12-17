from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer
from books.models import Book
from django.shortcuts import get_object_or_404

class BookReviewListCreate(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Review.objects.filter(book__id=book_id)

    def perform_create(self, serializer):
        book = get_object_or_404(Book, id=self.kwargs['book_id'])
        serializer.save(user=self.request.user, book=book)
