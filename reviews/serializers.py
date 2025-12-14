from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    book = serializers.ReadOnlyField(source='book.id')

    class Meta:
        model = Review
        fields = ['id', 'user', 'book', 'rating', 'review_text', 'created_at']
        read_only_fields = ('user', 'book', 'created_at')

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
