import logging
import time

from celery import chord, group, shared_task


@shared_task(time_limit=30, max_retries=0, name='casemgr.test_task', queue='normal')
def test_task(request=None):
    logging.info('test task starting')
    time.sleep(3)
    logging.info('test task completed')
    return 'test task completed!'
