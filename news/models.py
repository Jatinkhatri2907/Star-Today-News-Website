from django.db import models


class Article(models.Model):

    CATEGORY_CHOICES = [
        ("Politics", "Politics"),
        ("Technology", "Technology"),
        ("Sports", "Sports"),
        ("Business", "Business"),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to="news_images/", null=True, blank=True)
    content = models.TextField()
    summary = models.TextField(null=True, blank=True)
    views = models.IntegerField(default=0)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title