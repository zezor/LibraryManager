from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer, UserSerializer
from django.contrib.auth.models import User

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def checkout(self, request, pk=None):
        book = self.get_object()
        if not book.is_available:
            return Response({'error': 'Book is already checked out.'}, status=status.HTTP_400_BAD_REQUEST)
        book.is_available = False
        book.checked_out_by = request.user
        book.save()
        return Response({'message': 'Book checked out successfully.'})

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def return_book(self, request, pk=None):
        book = self.get_object()
        if book.is_available or book.checked_out_by != request.user:
            return Response({'error': 'You cannot return this book.'}, status=status.HTTP_400_BAD_REQUEST)
        book.is_available = True
        book.checked_out_by = None
        book.save()
        return Response({'message': 'Book returned successfully.'})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
