from rest_framework import viewsets, permissions
from .models import Book
from .serializers import BookSerializer

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
