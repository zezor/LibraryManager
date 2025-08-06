from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class BookSerializer(serializers.ModelSerializer):
    checked_out_by = UserSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'is_available', 'checked_out_by']

