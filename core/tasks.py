from celery import shared_task

# app = Celery('tasks', broker='redis://guest@localhost//')

@shared_task
def test_func():
	for i in range(10):
		print(i)
	return 'Shared task executed'