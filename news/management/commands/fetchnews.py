from django.core.management.base import BaseCommand
from news.fetch_news import fetch_news

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Fetching latest news...")
        fetch_news()
        print("News import completed.")