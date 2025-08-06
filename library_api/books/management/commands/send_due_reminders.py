from django.core.management.base import BaseCommand
from books.models import Borrow
from django.core.mail import send_mail
from datetime import date

class Command(BaseCommand):
    help = 'Send email reminders for due books'

    def handle(self, *args, **kwargs):
        due_today = Borrow.objects.filter(due_date=date.today(), returned=False)
        for borrow in due_today:
            send_mail(
                'Library Due Reminder',
                f'Dear {borrow.user.username}, your borrowed book "{borrow.book.title}" is due today.',
                'library@example.com',
                [borrow.user.email],
            )
        self.stdout.write(f'Sent {due_today.count()} reminders.')
