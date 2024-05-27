CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULTS_BACKEND= 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_BEAT_SHEDULER = 'django_celery_beat.shedulers:DatabaseSheduler'