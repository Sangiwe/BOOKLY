from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ['id','user','book','rating','review_text','created_at']
        read_only_fields = ('user','created_at')
