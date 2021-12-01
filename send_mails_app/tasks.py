from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from main_app import settings

User = get_user_model()

@shared_task
def send_mail_func():
    users = User.objects.all()
    for user in users:
        subject = 'Django Celery Integration Testing'
        message = '''I have integrated celery with the django to work with the taska in the background.
                    So that I can make django server to work more efficiently and faster'''
        to_email = user.email
        send_mail(
            subject= subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email,],
            fail_silently=True
        )
    return 'Sent Successfully'