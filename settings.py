# To schedule the task to run every 5 minutes 
# celery (message broker db), allows the tasks to run in the background, to free up the server for other tasks. It stores the task in redis db (for tasks, not objects). 

CELERY_BROKER_URL = 'redis://localhost:6379'
# URL where celery will store the results of the tasks it runs
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# to tell the app to check emergency lights every 5 minutes. 
CELERY_BEAT_SCHEDULE = {
    'check-emergency-lights-every-5-minutes': {
        'task': 'myapp.tasks.check_emergency_lights',
        'schedule': 300.0,
    },
}
