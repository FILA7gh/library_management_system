from django.conf import settings
from django.core.mail import send_mail


def send_notification(user, books):
    # if not books.exists():
    #     return
    #
    # book_list = "\n".join([f"- {book.title} (Автор: {book.author})" for book in books])
    book_list = []
    subject = "Новые книги за последние 24 часа"

    message = f"Здравствуйте, {user.username}!\n\nВот список новых книг, добавленных за последние 24 часа:\n\n{book_list}\n\n"

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        ["akmatbekovvv@gmail.com"],
        fail_silently=False,
    )
