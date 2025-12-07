from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer

class BookReviewListCreate(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        book_id = self.kwargs['book_id']
        return Review.objects.filter(book__id=book_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
