from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book, Borrow
from .serializers import BookSerializer, BorrowSerializer, UserSerializer
from django.contrib.auth.models import User
from django.core.mail import send_mail
from datetime import timedelta, date

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        borrow = self.get_object()
        borrow.returned = True
        borrow.save()
        borrow.book.available_copies += 1
        borrow.book.save()
        return Response({'status': 'book returned'})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
