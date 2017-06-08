from ..data_task import celery
import time

@celery.task(bind=True)
def task_test(self):
    for i in range(1,10):
        print i
        time.sleep(2)
