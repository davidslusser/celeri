import logging
import time

from celery import shared_task

from casemgr.helpers.bookings.spokane_county import get_roster


@shared_task(time_limit=30, max_retries=0, name="casemgr.test_task", queue="normal")
def test_task():
    logging.info("test task starting")
    time.sleep(3)
    logging.info("test task completed")
    return "test task completed!"


@shared_task(time_limit=30, max_retries=0, name="casemgr.get_roster", queue="normal")
def get_spokane_county_roster():
    logging.info("getting roster")
    get_roster()


@shared_task(time_limit=30, max_retries=0, name="casemgr.notify_booking", queue="normal")
def send_booking_notification(booking_id):
    logging.info(f"notify county clerk of new booking {booking_id}")
