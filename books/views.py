from rest_framework import viewsets, permissions, status
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_queryset(self):
        # only return user's books (or modify to return all if desired)
        return Book.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'])
    def start_reading(self, request, pk=None):
        book = self.get_object()
        book.status = Book.READING
        book.save()
        return Response(
            {"message": "Book marked as currently reading"},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'])
    def finish(self, request, pk=None):
        book = self.get_object()
        book.status = Book.READ
        book.save()
        return Response(
            {"message": "Book marked as read"},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'])
    def want_to_read(self, request, pk=None):
        book = self.get_object()
        book.status = Book.WANT_TO_READ
        book.save()
        return Response(
            {"message": "Book marked as want to read"},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=['post'])
    def drop(self, request, pk=None):
        book = self.get_object()
        book.status = Book.DROPPED
        book.save()
        return Response(
            {"message": "Book marked as dropped"},
            status=status.HTTP_200_OK
        )
