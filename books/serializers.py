from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ['id','title','author','isbn','cover_url','description','status','owner','date_added']
