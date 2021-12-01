from django.urls import path, include
from .views import test, send_mails_to_all, schedule_mail

urlpatterns = [
    path('test/', test, name='test'),
    path('send-mails-all/', send_mails_to_all, name='send-mails-all'),
    path('schedule-mail/', schedule_mail, name='schedule-mail')
]