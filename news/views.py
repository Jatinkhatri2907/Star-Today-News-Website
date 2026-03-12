from django.shortcuts import render
from .models import Article

def home(request):

    articles = Article.objects.all().order_by("-published_date")
    popular = Article.objects.all().order_by("-views")[:5]

    trending = Article.objects.all().order_by("-id")[:5]

    return render(request,"home.html",{
        "articles":articles,
        "popular":popular,
        "trending":trending
    })
def category_news(request, category):
    articles = Article.objects.filter(category=category)
    return render(request, 'home.html', {'articles': articles})
def article_detail(request, id):

    article = Article.objects.get(id=id)

    article.views += 1
    article.save()

    return render(request,"article.html",{"article":article})
def search_news(request):

    query = request.GET.get("q")

    articles = Article.objects.filter(title__icontains=query)

    return render(request,"home.html",{"articles":articles})