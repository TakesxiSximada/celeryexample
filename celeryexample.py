import time
from celery import Celery


app = Celery('tasks', broker='redis://localhost')

@app.task
def debug(name, count):
    time.sleep(count)
    return name
