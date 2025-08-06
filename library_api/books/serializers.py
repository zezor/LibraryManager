from rest_framework import serializers
from .models import Book, Borrow
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowSerializer(serializers.ModelSerializer):
    fine = serializers.SerializerMethodField()

    class Meta:
        model = Borrow
        fields = '__all__'

    def get_fine(self, obj):
        return obj.calculate_fine()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
