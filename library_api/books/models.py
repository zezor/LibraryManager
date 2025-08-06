from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    cover = models.ImageField(upload_to='book_covers/', blank=True, null=True)
    available_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    checkout_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    returned = models.BooleanField(default=False)

    def is_overdue(self):
        return not self.returned and self.due_date < date.today()

    def calculate_fine(self):
        if self.is_overdue():
            days = (date.today() - self.due_date).days
            return days * 1  # e.g. $1 per day
        return 0
