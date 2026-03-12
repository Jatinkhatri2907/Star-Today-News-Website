from apscheduler.schedulers.background import BackgroundScheduler
from .fetch_news import fetch_news


def start():

    print("Scheduler started")

    scheduler = BackgroundScheduler()

    # fetch news every 3 minutes
    scheduler.add_job(fetch_news, "interval", minutes=3)

    scheduler.start()