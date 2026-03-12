import requests
from .models import Article


API_KEY = "YOUR_API_KEY"


def fetch_news():

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    for item in data.get("articles", []):

        title = item.get("title")
        description = item.get("description")

        if title and not Article.objects.filter(title=title).exists():

            Article.objects.create(
                title=title,
                category="Technology",
                content=description if description else "No description available"
            )

            print("Added:", title)