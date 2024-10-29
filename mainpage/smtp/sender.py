from django.core.mail import get_connection


def smtp():
    connection = get_connection(
        host="smtp.gmail.com",
        port=587,
        username="omurkanovd22@gmail.com",
        password="zyjt glph lbrk vpdr",
        use_tls=True,
    )
    return connection
