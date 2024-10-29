from django.core.mail import get_connection
def smtp():
    connection = get_connection(
        host="smtp.gmail.com",
        port=587,
        username="nurdinovbaiel2005@gmail.com",
        password="vilq zrwk iuya oqfz",
        use_tls=True,
    )
    return connection
