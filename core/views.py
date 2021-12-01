from django.shortcuts import render
from .tasks import test_func
from django.http import HttpResponse
from send_mails_app.tasks import send_mail_func
from django_celery_beat.models import CrontabSchedule, PeriodicTask


def test(request):
	test_func.delay()
	return HttpResponse("Executed view")


def send_mails_to_all(request):
	send_mail_func.delay()
	return HttpResponse('Sent Mails Successfull')


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 17, minute = 34)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"5", task='send_mail_app.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
    return HttpResponse("Done")