from celery import shared_task
from datetime import timedelta
from django.utils import timezone
from apps.books.models import Book
from apps.users.models import CustomUser
from apps.users.utils import send_notification


@shared_task
def send_new_books_notification() -> None:
    now = timezone.now()
    yesterday = now - timedelta(days=1)

    new_books = Book.objects.filter(created_at__gte=yesterday)

    users = CustomUser.objects.all()
    for user in users:
        send_notification(user, new_books)


@shared_task
def send_anniversary_books_notification() -> None:
    today = timezone.now().date()
    anniversary_years = [5, 10, 20]

    for year in anniversary_years:
        target_date = today - timedelta(days=year * 365)
        anniversary_books = Book.objects.filter(
            publication_date=today.replace(year=target_date.year)
        )

        users = CustomUser.objects.all()
        for user in users:
            send_notification(user, anniversary_books)
