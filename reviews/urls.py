# reviews/urls.py
from django.urls import path
from .views import BookReviewListCreate

urlpatterns = [
    path('books/<int:book_id>/reviews/', BookReviewListCreate.as_view()),
]
